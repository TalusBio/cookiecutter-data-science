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

If you discover that you need an additional tool, all you need to do is add it
to your `environment.yaml` and run `make env` again.

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

# Import your functions and classes from 'src'
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
