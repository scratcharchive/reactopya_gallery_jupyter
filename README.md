# reactopya_gallery_jupyter

Jupyter notebook extension for the reactopy gallery

## Installation

You must first install the reactopy_gallery Python package. For convenience in development, this package is contained as a git submodule. (Note that this submodule contains its own git submodule).

Then install this python package

```
pip install -e .
```

Then compile the JavaScript and install the extension (in developer mode):

```
yarn install
jupyter nbextension install --py --symlink --sys-prefix reactopya_gallery_jupyter
jupyter nbextension enable reactopya_gallery_jupyter --py --sys-prefix
```

Then run jupyter notebook:

```
jupyter notebook
```

and open `example_notebooks/reactopya_gallery.ipynb`.

## Code generation

The Python and JavaScript wrappers needed for the Jupyter extension are automatically generated based on a configuration file. See the `code_generation/` directory.