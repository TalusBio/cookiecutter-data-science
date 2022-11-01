[![](static/talus-logo-full.svg){: style="height:75px"}](https://talus.bio)

# Data Science Project Template
---

Keeping well organized data science projects is difficult, but important.
Ideally every project should be reproducible---that is, anyone starting from
the same data, code, and similar hardware should be able to obtain the same 
results. 

The goal of this template is to make our data science work at Talus Bio
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

This template was inspired by the [The Cookiecutter Data Science
Project](http://drivendata.github.io/cookiecutter-data-science) and Bill
Noble's ["A Quick Guide to Organizing Computational Biology
Projects"](https://doi.org/10.1371/journal.pcbi.1000424).

## Principles Guiding This Template

Although this template is flexible, these principles guide its design:

### Data Analysis is **Non-Linear**

We try many things that work and even more that don't. Additionally, we often
have long running tasks that don't need to run again unless their dependencies
change. Thus, we can think of the tasks in a data analysis as a directed
acyclic graph (DAG), where each task has some defined set of dependencies and
an output which other tasks may depend on.

So how can we make the final analysis reproducible? We like to use GNU `make`. 
The `make` utility is common on MacOS and Linux systems and describes the 
dependency relationships between files. Given a `Makefile` (the file that 
defines these relationships), we can verify that our analysis completes the
same way from start to finish, every time.[^1]

[^1]: As your analyses grow, it may be beneficial to look at other tools, such
    [Snakemake](https://snakemake.readthedocs.io/en/stable/), to orchestrate
    your analyses.

We recommend editing the `run` rule in your `Makefile` to run your analyses and
create your final results in the `results` subdirectory. When this
recommendation is followed, an analysis can be completely regenerated with:

``` bash
$ make run
```

### Data is **Immutable**

The original data, whatever its form, is the starting point for all analyses
and should never be modified. Furthermore, transformations and modifications
that need to me made to the data should never be made manually and should never
overwrite the original data---such practices inevitability leads to
irreproducible analyses.

Instead, all alterations should be made programmatically and these intermediate
versions of the data can be saved alongside the original, if needed. Saving
intermediate files is most useful for transformations that take a long time to
perform. Otherwise, creating a reusable function to achieve the desired
transformation is typically more desirable.

All data should be stored in the `data` subdirectory, and it should **not** be
version controlled (don't add it to your git repository). Git should only be
used to track only files that are hand-edited---data should not be---and it is
often too large to work with in git effectively anyway. Additionally, even when
the data is small enough to feasibly manage in git, storing it in the
repository creates another point of potential leakage for data we need to keep
private: We don't want private data leaking because we accidently set a
repository to public!

When possible, data science projects should include a `sync` rule in their
`Makefile`. This rule should download the data needed to run all of the
analyses that are part of the project. We have this rule configured to pull
data from specified subdirectories of a specified Amazon Web Services (AWS) S3
bucket by default. However, this rule can be configured to pull data from
anywhere that your data is stored.[^2] For any project following these
guidelines, you can synchronize your data directory with:

``` bash
$ make sync
```

[^2]: If you're using public mass spectrometry data from MassIVE or PRIDE,
    consider using [ppx](https://ppx.readthedocs.io) to download the data
    reproducibly.

### Notebooks are for **Exploration** and **Communication**

Notebook packages like the Jupyter notebook and other literate programming
tools are very effective for exploratory data analysis. However, these tools
can be less effective for reproducing an analysis. Since notebooks are
challenging objects for version control (e.g., diffs of the json are often not
human-readable and merging is near impossible), we recommended not
collaborating directly with others on the same Jupyter notebook. We recommend
these steps for using notebooks effectively:

- Jupyter notebooks are stored in the `notebooks` subdirectory. Typically we
  store notebooks in their final state, which makes them easy to share with
  team members.
  
- We like to use additional subdirectories to divide different types of analyses,
  particularly for projects that take place over longer periods of time. We
  recommend the format `<date>_<description>` for these directories (e.g.,
  `2021-07-08_exporatory-analyses`). If multiple people are writing notebooks
  in the same repository, we recommend an additional subdirectory
  specifying the GitHub username of the notebook authors. For instance, I may
  have a notebook here:
  ```
  notebooks/wfondrie/2021-07-08_exploratory-analyses/1_visualizations.ipynb
  ```
  
- Follow a naming convention that shows the order in which the analysis was
  performed. We recommend the format `<step>_<description>.ipynb` (e.g.,
  `0.3_visualize-distributions.ipynb`).

- Refactor the good parts. Don't write code to do the same task in multiple
  notebooks. If it's a data preprocessing task, put it in the pipeline at
  `src/make_dataset.py` and load data from data/interim. If it's useful
  utility code, refactor it to `src`. Also, don't be afraid to write useful
  scripts alongside your notebooks. Finally, if you find yourself writing the
  same code for multiple projects, consider writing a Python Package. See my
  [cookiecutter
  template](https://github.com/wfondrie/cookiecutter-python-package) for a good
  starting point.
  
- Jupyter notebooks are designed for literate programming, so take advantage!
  Create markdown cells that describe the experiments contained within the
  notebook and the different stages of analysis, as well as key results.
  
- Be consistent with how you save results. I store all of my figures in a
  `figures` subdirectory alongside my notebooks. Additionally, these should not
  be version controlled, unless there is a specific reason to do so.

### **Reproducibility** Starts With the Environment

Our environment defines the tools, including their versions, that we need to
complete our analyses. To manage your environment, we recommend using [the
conda package manager](https://docs.conda.io/en/latest/). Why conda? Although
largely thought of as a Python package manager, conda can download and install
a wide variety of useful software in a reproducible manner. For example, one of
the proteomics tools we routinely use is a Java program,
[EncyclopeDIA](https://bitbucket.org/searleb/encyclopedia/wiki/Home), and
available through the [bioconda channel](https://bioconda.github.io/).

Once we know what software we need, we can complete the `environment.yaml` file,
which will allow anyone to install the same software and reproduce our
analysis. When ready, create your environment using this file with:

``` bash
$ make env
```
