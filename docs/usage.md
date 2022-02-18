# How to Use This Template 

## 1. Install Dependencies
 
 - Python 3.6+ - We recommend through
   [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
 - [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html) >=
   1.4.0
   
 Cookiecutter can be installed with pip by or conda depending on how you manage
 your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## 2. Start a New Project

To start a new data science project first run:

``` bash
$ cookiecutter gh:TalusBio/cookiecutter-data-science
```

After running the command you will be directed through a series of prompts to
finish setting up your project. The directory structure of your new project
will look like this:

```
├── LICENSE
├── Makefile           <- Makefile with commands like `make sync` or `make run`.
├── README.md          <- The top-level README for developers using this project.
├── data               <- The original, immutable data.
├── docs               <- Manuscript drafts, presentations, etc.
├── notebooks          <- Jupyter notebooks. See above for the naming convention.
├── results            <- Generated analyses, such as figures and reports. 
│                         Results should only be added to this directory using a
│                         a GNU make rule.
├── environment.yaml   <- Specifies the dependencies to build a conda environment.
├── pyproject.toml     <- Specifies Python build tools and settings (flake8, black, etc.)
├── setup.cfg          <- Defines metadata about the project. 
├── setup.py           <- Makes project pip installable (pip install -e .) so src can 
│                         be imported as a Python package.
├── src                <- Source code for use in this project.
│   └── __init__.py    <- Makes src a Python module.
└── .env               <- Define sensitive environment variables. This is intentionally 
                          ignored by git by default. Do not commit this file!
```

Feel free to modify these directories and files as best fits your needs. For
example, if your project does not use Python, you may want to remove a few
files: `pyproject.toml`, `setup.cfg`, `setup.py`, and `src/__init__.py`.


## 3. Customize and Do Cool Things

Your first task in your new project should be to edit `environment.yaml`, so
that it contains all of the software dependencies for your project. Once it 
is ready, create your project environment with:

```bash
$ make env
```

Then follow the instructions to activate your new environment. With your
environment prepared and activated, you're ready to start your analyses!
