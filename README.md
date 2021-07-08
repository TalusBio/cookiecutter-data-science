# A template for data science projects at Talus Bio

Keeping well organized data science projects is difficult, but important.
Ideally every project should be reproducible---that is, anyone starting from
the same data, code, and similar hardware should be able to obtain the same 
results. 

The goal of this template is to make our data science work at Talus
reproducible and approachable. Using this template ensures that we organize
code and data consistently across projects. This means when you join another
project that is organized using this template, you will immediately know the
lay of the land. 

This template uses [cookiecutter](https://github.com/cookiecutter/cookiecutter)
to create a directory structure for a repository that is consistent and
well-suited for data science projects. There are biases and assumptions in this
template: we assume that Python will be your primary tool (although it doesn't
have to be) and that some amount of modeling will be performed as part of the 
project (although there doesn't have to be). As such, this template is intended
to serve as a guideline rather than a rule and you should feel free to modify
it as needed for your specific project.

This template was adapted from the [The Cookiecutter Data Science
Project](http://drivendata.github.io/cookiecutter-data-science)

## Principles guiding this template

Although this template is flexible, there are a few principles that guide its
design.

### Data is immutable

The original data, whatever its form, is the starting point for all analyses
and should never be modified. Furthermore, transformations and modifications
that need to me made to the data should never be made manually and should never
overwrite the original data---such practices inevitability leads to
irreproducible analyses.

Instead, all alterations should be made programmatically and these intermediate
versions of the data can be saved alongside the original, if needed.

### Notebooks are for exploration and communication

Notebook packages like the Jupyter notebook and other literate programming
tools are very effective for exploratory data analysis. However, these tools
can be less effective for reproducing an analysis. Since notebooks are
challenging objects for source control (e.g., diffs of the json are often not
human-readable and merging is near impossible), we recommended not
collaborating directly with others on Jupyter notebooks. There are three steps
we recommend for using notebooks effectively:

- Follow a naming convention that shows the owner and the order the analysis
  was done in. We recommend the format `<step>_<ghuser>_<description>.ipynb`
  (e.g., `0.3_wfondrie_visualize-distributions.ipynb`).

- Refactor the good parts. Don't write code to do the same task in multiple
  notebooks. If it's a data preprocessing task, put it in the pipeline at
  `src/data/make_dataset.py` and load data from data/interim. If it's useful
  utility code, refactor it to `src`.
  
- We like to use subdirectories to divide different types of analyses,
  particularly for projects that take place over longer periods of time. We
  recommend the format `<date>_<ghuser>_<description>` for these directories
  (e.g., `2021-07-08_wfondrie_exporatory-analyses`).


### Data analysis is non-linear

We try many things that work and even more that don't. Additionally, we often
have long running tasks that don't need to run again unless their dependencies
change. Thus, we can think of the tasks in a data analysis as a directed
acyclic graph (DAG), where each task has some defined set of dependencies and
an output which other tasks may depend on.

So how can we make the final analysis reproducible? We like to use GNU `make`. 
The `make` utility is common on MacOS and Linux systems and describes the 
dependency relationships between files. Given a `Makefile` (the file that 
defines these relationships), we can verify that our analysis completes the
same way from start to finish, every time.

### Reproducibility starts with the environment

Our environment defines the tools, including their versions, that we need to
complete our analyses. To manage your environment, we recommend using [the
conda package manager](https://docs.conda.io/en/latest/). Why conda? Although
largely thought of as a Python package manager, conda can download and install
a wide variety of useful software in a reproducible manner. For example,
EncyclopeDIA is available through the [bioconda
channel](https://bioconda.github.io/).

Once we know what software we need, we can complete the `environment.yml` file,
which will allow anyone to install the same software and reproduce our
analysis.


## Requirements to use this template.
 
 - Python 3.6+ - We recommend through
   [Miniconda](https://docs.conda.io/en/latest/miniconda.html).
 - [Cookiecutter](http://cookiecutter.readthedocs.org/en/latest/installation.html) >=
   1.4.0
   
 This can be installed with pip by or conda depending on how you
 manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

## Starting a new project:

To start a new data science project first run:

``` bash
$ cookiecutter https://github.com/TalusBio/cookiecutter-talus-data-science
```

After running the command you will be directed through a series of prompts to
finish setting up your project. The directory structure of your new project
will look like this:

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

Feel free to modify these directories and files as best fits your needs. For
example, if your project does not use Python, you may want to remove a few
files: `pyproject.toml`, `setup.cfg`, `setup.py`, and `src/__init__.py`.

Now go forth and do cool things!

## Tips and Tricks

### Setting up your environment

First make sure that your `environment.yml` contains the tools you need for
your analysis. The `Makefile` included in the repository already contains
the rules to create or update the environment for your project, based on 
the `environment.yml`. From the root of your project, run:

``` bash
$ make env
```

Then go ahead and activate your new environment, replacing `{project name}` 
with the name of your project:

``` bash
$ conda activate {project name}
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
