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
        "certifi",
        "colorama",
        "coverage",
        "Cython",
        "cycler",
        "decorator",
        "docutils",
        "flake8",
        "futures",
        "husl",
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
        "nose",
        "notebook",
        "notedown",
        "numpy",
        "openpyxl",
        "path.py",
        "pbr",
        "pandas",
        "pep8",
        "pexpect" if not sys.platform.startswith("win") else None,
        "pickleshare",
        "pipdeptree",
        "psutil",
        "ptyprocess" if not sys.platform.startswith("win") else None,
        "pycparser",
        "pyflakes",
        "pygments",
        "pyparsing",
        'pypiserver',
        "python-dateutil",
        "python-jenkins",
        "pytz",
        "pywin32" if sys.platform.startswith("win") else None,
        "pyzmq",
        "qtconsole",
        "requests",
        "simplegeneric",
        "six",
        "sphinx",
        'sphinxcontrib-images',
        'snowballstemmer',
        'sphinx-rtd-theme',
        "sphinxjp.themes.revealjs",
        "terminado" if not sys.platform.startswith("win") else None,
        "tornado",
        "traitlets",
        "virtualenv",
        "wheel",
        "wild_sphinx_theme",
        "winshell" if sys.platform.startswith("win") else None,
    ]

    from . import find_module_install
    return [find_module_install(_) for _ in names if _ is not None]
