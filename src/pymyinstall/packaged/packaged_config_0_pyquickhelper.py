#-*- coding: utf-8 -*-
"""
@file
@brief Defines different a set of usual modules for Python.
"""
import sys


def pyquickhelper_set():
    """
    list of modules needed to run unit test of module *pyquickhelper*
    """
    names = [
        "alabaster",
        "autopep8",
        "babel",
        "backports.shutil-get-terminal-size",
        "bleach",
        "brewer2mpl",
        "certifi",
        "codecov",
        "colorama",
        "coverage",
        "Cython",
        "cycler",
        "decorator",
        "docutils",
        "entrypoints",
        "et_xmlfile",
        "flake8",
        "husl",
        "html5lib",
        "imagesize",
        "ipython",
        "ipykernel",
        "ipystata" if sys.version_info[0] == 2 else None,
        "ipython_genutils",
        "ipywidgets",
        "jinja2",
        "jsonschema",
        "jupyter-console",
        "jupyter",
        "jupyter_core",
        "jupyter_client",
        "jupyter-pip",
        "jupyter_sphinx",
        "jyquickhelper",
        "keyring",
        "lxml",
        "matplotlib",
        "metakernel",
        "micropython-libc" if not sys.platform.startswith("win") else None,
        "micropython-ffilib" if not sys.platform.startswith(
            "win") else None,
        "micropython-fcntl" if not sys.platform.startswith(
            "win") else None,
        'markupsafe',
        "mccabe",
        "mistune",
        "multi_key_dict",
        "nbformat",
        "nbconvert",
        "nbpresent",
        "nose",
        "backports_abc",
        "notebook",
        "notedown",
        "numpy",
        "jdcal",
        "openpyxl",
        "path.py",
        "pbr",
        "pandas",
        "pandoc-attributes",
        "pandocfilters",
        "patsy",
        "pep8",
        "pexpect",  # if not sys.platform.startswith("win") else None,
        "pickleshare",
        "pipdeptree",
        "prompt_toolkit",
        "psutil",
        "ptyprocess",  # if not sys.platform.startswith("win") else None,
        "pycodestyle",
        "pycparser",
        "pycrypto",
        "pycryptodomex",
        "pyflakes",
        "pygments",
        "pyparsing",
        'pypiserver',
        "python-dateutil",
        "python-jenkins",
        "pytz",
        "pywin32" if sys.platform.startswith("win") else None,
        "pywin32-ctypes" if sys.platform.startswith("win") else None,
        "pyzmq",
        "qtconsole",
        "requests",
        "simplegeneric",
        "six",
        "sphinx",
        "sphinx_gallery",
        'sphinxcontrib-images',
        'sphinxcontrib-imagesvg',
        'sphinxcontrib-jsdemo',
        'snowballstemmer',
        'sphinx-rtd-theme',
        "sphinxjp.themes.revealjs",
        'tabulate',
        'tqdm',
        "terminado" if not sys.platform.startswith("win") else None,
        "testpath",
        "tornado",
        "traitlets",
        "virtualenv",
        "xlrd",
        "wcwidth",
        "webencodings",
        "wheel",
        "widgetsnbextension",
        "wild_sphinx_theme",
        "win_unicode_console",
        "winrandom" if sys.platform.startswith("win") else None,
        "winshell" if sys.platform.startswith("win") else None,
    ]

    from .automate_install import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
