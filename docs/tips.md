# Tips and Tricks

## Setting up Your Conda Environment

First make sure that your `environment.yaml` contains the tools that you need
for your analysis. The `Makefile` included in the repository already contains
the rules to create or update the environment for your project, based on the
`environment.yaml`. From the root of your project, run:

``` bash
$ make env
```

This will install your conda environment directly into the root of the
repository. Follow the instructions to activate your new environment.

**Tip:** Your shell prompt now likely shows the full path to your conda
environment, which may be unwieldy. Update your conda config to hide this with:

``` bash
conda config --set env_prompt '({name})'
```

## The `src` Directory Works Like a Python Package!

The default files we include allow the `src` directory to work like a Python
package. If you've installed and activated your environment above, then its
ready to go! You can now use the functions and classes defined in `src` within
your Jupyter notebooks:

```jupyter-notebook
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```

## Enable Python Code Formatting With Black

[Black](https://black.readthedocs.io/en/stable/) is a Python code formatting
tool that helps us maintain uniform code formats throughout our projects.
The easiest way to use Black is to set it up as a pre-commit hook. This way
Black will run whenever you commit changes to your repository.

To enable Black, run from the root of your project:

``` bash
$ pre-commit install
```

## Create a Config File For Easy Project Creation

It can be tedious to always have to type in your name, S3 bucket, and file
patterns for every new project if they are almost always the same. One way
to avoid this is to create a [user config file](https://cookiecutter.readthedocs.io/en/2.0.2/advanced/user_config.html). 
For example, I created `~/dsproj.yaml` which looks like this:

```yaml
default_context:
    author_name: "William E Fondrie"
    open_source_license: "MIT"
    s3_bucket: "data-pipeline-experiment-bucket"
    s3_file_patterns: "*.peptides.txt *.proteins.txt *proteins.csv"
```

Then I use it when I create a project:
```bash
$ cookiecutter --config-file ~/dsproj.yaml gh:TalusBio/cookiecutter-data-science
```
