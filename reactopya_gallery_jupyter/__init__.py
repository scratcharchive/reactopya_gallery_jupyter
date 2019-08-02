from .all_widgets import *

from ._version import version_info, __version__

def _jupyter_nbextension_paths():
    return [{
        'section': 'notebook',
        'src': 'static',
        'dest': 'reactopya_gallery_jupyter',
        'require': 'reactopya_gallery_jupyter/extension'
    }]
