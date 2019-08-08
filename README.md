# reactopya_gallery_jupyter

Jupyter notebook extension for the reactopy gallery

## Installation

You must first install the reactopya_gallery Python package. For convenience in development, this package is contained as a git submodule. (Note that the reactopya_gallery submodule contains its own git submodule!).

```
git clone --recursive [URL to Git repo]
```

Or if you have already cloned, then do:

```
git submodule update --init
```

Then install this python package

```
pip install -e .
```

Next, compile the JavaScript and install the extension (in developer mode):

```
yarn install
jupyter nbextension install --py --symlink --sys-prefix reactopya_gallery_jupyter
jupyter nbextension enable reactopya_gallery_jupyter --py --sys-prefix
```

Finally, run jupyter notebook:

```
jupyter notebook
```

and open `example_notebooks/reactopya_gallery.ipynb`.

## Update

For subsequent pulls, make sure to recursively pull all submodules:

```
git pull --recurse-submodules
```

To apply these changes, run:
```
yarn install
```
then reload the notebook (both kernel and browser page). This assumes also that the extension was installed as a symlink (i.e., development mode).


## Code generation

The Python and JavaScript wrappers needed for the Jupyter extension are automatically generated. See the `code_generation/` directory.
