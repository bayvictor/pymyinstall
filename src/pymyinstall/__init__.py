#-*- coding: utf-8 -*-
"""
Documentation for this file.

To install a list of modules for a machine learner:
@code
from pymyinstall import complete_installation, install_scite, install_pandoc, open_tool_on_browser
for _ in complete_installation() :
    _.install(temp_folder="install")
install_scite("install")
install_pandoc("install")
open_tool_on_browser()
@endcode
"""

__version__ = "1.1"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pymyinstall"
__url__ = "http://www.xavierdupre.fr/app/pymyinstall/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#pymyinstall"
__license__ = "MIT License"


def _setup_hook():
    """
    does nothing
    """
    # we clean the cache
    import os
    if os.path.exists(ModuleInstall._page_cache_html):
        os.remove(ModuleInstall._page_cache_html)


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.
    If you want to disable the logs:

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True

from .installhelper.install_cmd_helper import run_cmd, unzip_files
from .installhelper.module_install import ModuleInstall
from .installcustom.install_custom import download_from_sourceforge, download_file, download_page
from .installhelper.install_manual import get_install_list
from .installhelper import get_module_version, get_pypi_version
from .installcustom.install_custom_revealjs import download_revealjs
from .installhelper.requirements import build_requirements
from .win_installer.win_setup_main import win_python_setup
from .packaged import install_module, update_module, download_module
