# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- Manuscript drafts, presentations, etc.
│
├── models             <- Trained and serialized models.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's GH username, and a short `-` delimited description, e.g.
│                         `1.0-wfondrie-initial-data-exploration`.
│
├── results            <- Generated analyses, such as figures and reports.
│
├── environment.yml    <- Specifies the dependencies to build a conda environment.
│                         Create the environment with `conda env create -f environment.yml`
│
├── pyproject.toml     <- Specifies Python build tools and setttings (flake8, black, etc.)
│
├── setup.cfg          <- Defines metadata about the project. 
│
├── setup.py           <- Makes project pip installable (pip install -e .) so src can be imported
│
└── src                <- Source code for use in this project.
    └── __init__.py    <- Makes src a Python module
```

This project is based on the [Talus Cookiecutter Data Science Template](https://github.com/TalusBio/cookiecutter-data-science)

## Tips and Tricks

### Setting up your environment

First make sure that your `environment.yml` contains the tools you need for
your analysis. The `Makefile` included in the repository already contains
the rules to create or update the environment for your project, based on 
the `environment.yml`. From the root of your project, run:

``` bash
$ make env
```

Then go ahead and activate your new environment

``` bash
$ conda activate {{ cookiecutter.repo_name }}
```

### The `src` directory works like a Python package!

The default files we include allow the `src` directory to work like a Python
package. If you've installed and activate you're environment above, then its
ready to go! You can now use the functions and classes defined in `src` within
your Jupyter notebooks:

``` jupyter-notebook
# OPTIONAL: Load the "autoreload" extension so that code can change
%load_ext autoreload

# OPTIONAL: always reload modules so that as you change code in src, it gets loaded
%autoreload 2

from src.data import make_dataset
```

### Enable Python code formatting with black

[Black](https://black.readthedocs.io/en/stable/) is a Python code formatting
tool that helps us maintain uniform code formats throughout our projects.
The easiest way to use Black is to set it up as a pre-commit hook. This way
Black will run whenever you commit changes to your repository.

To enable Black, run from the root of your project:

``` bash
$ pre-commit install
```
