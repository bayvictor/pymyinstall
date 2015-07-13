"""
@file
@brief Creates batch file to set up the environment
"""
from __future__ import print_function

import os


def create_win_batches(folders, verbose=False, selection=None, fLOG=print, module_list=None):
    """
    create batchs for the setup, they will be placed in
    *folders["config"]*

    @param      folders     dictionary with the keys *tools*, *config*, *python*, *workspace*
    @param      verbose     verbose
    @param      fLOG        logging function
    @param      selection   list of batchs to create
    @param      module_list list of python modules to install, to know which script to install or not
    @return                 operations (list of what was done)
    """
    if selection is None:
        raise ValueError("selection cannot be None")
    if module_list is None:
        raise ValueError("module_list cannot be None")

    has_ipython = False
    has_rodeo = False
    has_spyder = False
    has_rss = False
    for mod in module_list:
        if mod.name == "IPython":
            has_ipython = True
        if mod.name == "rodeo":
            has_rodeo = True
        if mod.name == "spyder":
            has_spyder = True
        if mod.name == "pyrsslocal":
            has_rss = True

    list_functions = [create_win_env,
                      create_win_scite,
                      create_win_sqllitespy,
                      create_win_python_console,
                      win_replace_shebang,
                      ]

    if has_ipython:
        list_functions.extend([create_win_ipython_console,
                               create_win_ipython_qtconsole,
                               create_win_ipython_notebook,
                               win_install_kernels,
                               ])

    if has_rodeo:
        list_functions.append(create_win_rodeo)

    if has_spyder:
        list_functions.append(create_win_spyder)

    if has_rss:
        list_functions.append(create_win_rss)

    if "r" in selection:
        list_functions.append((create_win_r_console, "r"))
        list_functions.append((create_win_r_gui, "r"))

    if "julia" in selection:
        list_functions.append((create_win_julia_console, "julia"))

    operations = []
    for func in list_functions:
        if isinstance(func, tuple):
            func, name = func
        else:
            name = None

        if name is None or name in selection:
            op = func(folders)
            if verbose:
                for o in op:
                    fLOG(" ".join(o))
            operations.extend(op)
    return operations


def create_win_env(folders):
    """
    create a batch file to set up the environment

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    tools = folders["tools"]
    text = ["@echo off", "set CURRENT=%~dp0",
            "set PYTHON_WINHOME=%CURRENT%\\..\\python",
            "set PYTHON_WINSCRIPTS=%CURRENT%\\..\\python\\Scripts",
            "set WORKSPACE=%CURRENT%\\..\\workspace",
            "set PATH=%PYTHON_WINHOME%;%PATH%"]
    if os.path.exists(os.path.join(tools, "R")):
        text.append("set R_HOME=%CURRENT%\\..\\tools\\R")
        text.append("set R_LIBS=%CURRENT%\\..\\tools\\R\\library")
    if os.path.exists(os.path.join(tools, "Julia")):
        text.append("set JULIA_HOME=%CURRENT%\\..\\tools\\Julia")
        text.append("set JULIA_PKGDIR=%CURRENT%\\..\\tools\\Julia\\pkg")
    if os.path.exists(os.path.join(tools, "MinGW")):
        text.append("set PATH=%PATH%;%CURRENT%\\..\\tools\\MinGW\\bin")

    text = "\n".join(text)
    name = os.path.join(folders["config"], "env.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_ipython_console(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off",
            "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %WORKSPACE%",
            "%IPYTHON% --ipython-dir=%CURRENT2% --profile=win_profile"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_console.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_ipython_qtconsole(folders):
    """
    create a batch file to start ipython QtConsole

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %WORKSPACE%",
            "start %IPYTHON% qtconsole --ipython-dir=%CURRENT2% --profile=win_profile"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_qtconsole.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_ipython_notebook(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set IPYTHON=%CURRENT2%\\..\\python\\Scripts\\ipython.exe",
            "cd %WORKSPACE%",
            "%IPYTHON% notebook --notebook-dir=%CURRENT2%\\..\\workspace --ipython-dir=%CURRENT2% --profile=win_profile"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "ipython_notebook.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_rodeo(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set RODEO=%CURRENT2%\\..\\python\\Scripts\\rodeo.exe",
            "cd %WORKSPACE%",
            "%RODEO% %CURRENT2%\\..\\workspace"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "rodeo.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_scite(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set SCITE=%CURRENT2%\\..\\tools\\Scite\\wscite\\scite.exe",
            "cd %WORKSPACE%",
            "start %SCITE% %1"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "scite.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_sqllitespy(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set SQLITESPY=%CURRENT2%\\..\\tools\\SQLiteSpy\\SQLiteSpy.exe",
            "cd %WORKSPACE%",
            "start %SQLITESPY%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "sqlitespy.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_python_console(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set PYTHON=%CURRENT2%\\..\\python\\python.exe",
            "cd %WORKSPACE%",
            "%PYTHON%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "python_console.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_julia_console(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "rem call %CURRENT2%\\env.bat",
            "set JULIA=%CURRENT2%\\..\\tools\\Julia\\bin\\julia.exe",
            "cd %CURRENT2%\\..\\workspace",
            "%JULIA%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "julia_console.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_spyder(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "cd %CURRENT2%\\..\\python\\Scripts",
            "spyder.exe --workdir=%WORKSPACE%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "spyder.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_r_console(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set REXE=%CURRENT2%\\..\\tools\\R\\bin\\x64\\R.exe",
            "cd %WORKSPACE%",
            "%REXE%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "r_console.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_r_gui(folders):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            "set RGUI=%CURRENT2%\\..\\tools\\R\\bin\\x64\\Rgui.exe",
            "cd %WORKSPACE%",
            "start %RGUI%"]

    text = "\n".join(text)
    name = os.path.join(folders["config"], "r_gui.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def win_install_kernels(folders, suffix=""):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @param      suffix      add a suffix
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            '%PYTHON_WINHOME%\\python -c "from pymyinstall.win_installer import inno_install_kernels;inno_install_kernels(\'CURRENT2\', \'%1\')"']

    text = "\n".join(text)
    name = os.path.join(folders["config"], "add_kernels.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def win_replace_shebang(folders, suffix=""):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @param      suffix      add a suffix
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            'if "%1"=="" (',
            '    set P1=EMPTY_STRING',
            ') ELSE (',
            '    set P1=%1',
            ')',
            'if "%2"=="" (',
            '    set P2=%PYTHON_WINHOME%',
            ') ELSE (',
            '    set P2=%2',
            ')',
            '%PYTHON_WINHOME%\\python -c "import os;from pymyinstall.win_installer import win_patch_paths;win_patch_paths(\'PYTHON_WINSCRIPTS\', [\'\', \'P1\'], \'P2\')"']

    text = "\n".join(text)
    name = os.path.join(folders["config"], "replace_shebang.bat")
    with open(name, "w") as f:
        f.write(text)
    return [("batch", name)]


def create_win_rss(folders, suffix=""):
    """
    create a batch file to start ipython

    @param      folders     see @see fn create_win_batches
    @param      suffix      add a suffix
    @return                 operations (list of what was done)
    """
    text = ["@echo off", "set CURRENT2=%~dp0",
            "call %CURRENT2%\\env.bat",
            '%PYTHON_WINHOME%\\python -c "from pyquickhelper import fLOG;from pyquickhelper.pycode.blog_helper import rss_update_run_server;fLOG(OutputPrint=True);rss_update_run_server(r\'%CURRENT2%rss_database.db3\', r\'%CURRENT2%rss_list.xml\')"']

    text = "\n".join(text)
    name = os.path.join(folders["config"], "run_fetch_rss.bat")
    with open(name, "w") as f:
        f.write(text)

    text = """
                <?xml version="1.0" encoding="UTF-8"?>
                <opml version="1.0">
                    <head>
                        <title>teachings subscriptions</title>
                    </head>
                    <body>
                        <outline text="XD blog" title="XD blog" type="rss"
                            xmlUrl="http://www.xavierdupre.fr/blog/xdbrss.xml"
                            htmlUrl="http://www.xavierdupre.fr/blog/xd_blog.html" />
                    </body>
                </opml>
                """.replace("                ", "")

    rss_name = os.path.join(folders["config"], "rss_list.xml")
    with open(rss_name, "w", encoding="utf8") as f:
        f.write(text)

    return [("batch", name), ("rss", rss_name)]
