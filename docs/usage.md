# How to Use This Template 

## 1. Install Dependencies

To use this template, you'll need to install these dependencies:
 
 - Python 3.9+ - We recommend through
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


Feel free to modify these directories and files as best fits your needs. For
example, if your project does not use Python, you may want to remove a couple
files: `pyproject.toml` and `src/__init__.py`.


## 3. Customize and Do Cool Things

Your first task in your new project should be to edit `environment.yaml`, so
that it contains all of the software dependencies for your project. Once it 
is ready, create your project environment with:

```bash
$ make env
```

Then follow the instructions to activate your new environment. With your
environment prepared and activated, you're ready to start your analyses!
