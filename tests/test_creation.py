import os
import pytest
from subprocess import check_output
from conftest import system_check
from contextlib import contextmanager


@contextmanager
def cwd(path):
    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("default_baked_project")
class TestCookieSetup(object):
    def check(self, arg):
        args = ["python", "setup.py", "--" + str(arg)]
        with cwd(self.path):
            p = check_output(args).decode("ascii").strip()

        return p

    def test_project_name(self):
        project = self.path
        if pytest.param.get("project_name"):
            name = system_check("TalusBio")
            assert project.name == name
        else:
            assert project.name == "project_name"

    def test_author(self):
        p = self.check("author")
        if pytest.param.get("author_name"):
            assert p == "Will"
        else:
            assert p == "Your name (or your organization/company/team)"

    def test_readme(self):
        readme_path = self.path / "README.md"
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get("project_name"):
            with open(readme_path) as fin:
                assert "# TalusBio" == next(fin).strip()

    def test_setup(self):
        p = self.check("version")
        assert p == "0.1.0"

    def test_license(self):
        license_path = self.path / "LICENSE"
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        p = self.check("license")
        if pytest.param.get("open_source_license"):
            assert p == "BSD-3"
        else:
            assert p == "MIT"

    def test_environment(self):
        reqs_path = self.path / "environment.yml"
        assert reqs_path.exists()
        assert no_curlies(reqs_path)

    def test_makefile(self):
        makefile_path = self.path / "Makefile"
        assert makefile_path.exists()
        assert no_curlies(makefile_path)

    def test_folders(self):
        expected_dirs = [
            "data",
            "docs",
            "notebooks",
            "results",
            "src",
        ]

        ignored_dirs = [str(self.path)]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))
        assert len(set(abs_expected_dirs + ignored_dirs) - set(abs_dirs)) == 0
