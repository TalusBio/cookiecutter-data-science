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

This template was adapted from the [The Cookiecutter Data Science
Project](http://drivendata.github.io/cookiecutter-data-science)


## Requirements to use this cookiecutter template:
 
 - Python 3.5+
 - [Cookiecutter Python
   package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >=
   1.4.0: This can be installed with pip by or conda depending on how you
   manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


## To start a new project, run:

``` bash
$ cookiecutter -c v1 https://github.com/talusbio/cookiecutter-data-science
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
├── docs               <- A default Sphinx project; see sphinx-doc.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
└── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
```

## Installing development requirements

    pip install -r requirements.txt

## Running the tests

    pytest tests
