# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

```
├── Makefile                       <- Makefile with commands like `make data` or `make env`
├── README.md                      <- The top-level README for developers using this project.
├── data                           <- The original, immutable data.
├── docs                           <- Manuscript drafts, presentations, etc.
├── notebooks                      <- Jupyter notebooks and/or analysis scripts. 
│   └── wfondrie                   <- Create a subdirectory with your username.
│       └── 2022-11-01_my-analysis <- Create a dated subdirectory for each analysis.
│           ├── notebook.ipynb     <- The analysis notebook or script.
│           └── figures            <- A subdirectory to put the generated figures
├── environment.yml                <- Specifies the dependencies to build a conda environment.
│                                     Create the environment with `make env && conda activate ./envs`
├── pyproject.toml                 <- Specifies Python configuration for our local Python package.
├── src                            <- Source code for the local Python package to use in this project.
│   └── __init__.py                <- Makes src a Python module
└── .env                           <- Define sensitive environment variables. This is intentionally 
                                      ignored by git by default. Do not commit this file!
```

This project is based on the [Talus Cookiecutter Data Science
Template](https://github.com/TalusBio/cookiecutter-data-science)

## Tips and Tricks

### Setting up your environment

First make sure that your `environment.yml` contains the tools you need for
your analysis. The `Makefile` included in the repository already contains
the rules to create or update the environment for your project, based on 
the `environment.yml`. From the root of your project, run:

``` bash
$ make env
```

This will install your conda environment directly into the root of the
repository, in the `envs` directory. To go ahead and activate your new
environment:

``` bash
$ conda activate ./envs
```

**Tip:** Your shell prompt now likely shows the full path to your conda
environment, which may be unwieldy. Update your conda config to hide this with:

``` bash
conda config --set env_prompt '({name})'
```

### The `src` directory works like a Python package!

The default files we include allow the `src` directory to work like a Python
package. If you've installed and activated your environment above, then its
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
