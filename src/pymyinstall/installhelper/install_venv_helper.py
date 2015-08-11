"""
@file
@brief Helpers for virtualenv
"""
from __future__ import print_function

import os
import sys
from .install_cmd_helper import run_cmd


class VirtualEnvError(Exception):
    """
    exception raised by the function implemented in this file
    """
    pass


def build_venv_cmd(params, posparams):
    """
    builds the command line for virtual env

    @param      params      dictionary of parameters
    @param      posparams   positional arguments
    @return                 string
    """
    import venv
    exe = sys.executable
    cmd = [exe, "-m", "venv"]
    for k, v in params.items():
        if v is None:
            cmd.append("--" + k)
        else:
            cmd.append("--" + k + "=" + v)
    cmd.extend(posparams)
    return " ".join(cmd)


def create_virtual_env(where, symlinks=False, system_site_packages=False,
                       clear=True, packages=None, fLOG=print,
                       temp_folder=None):
    """
    .. index:: virtual environment

    create a virtual environment

    @param      where                   location of this virtual environment
    @param      symlinks                attempt to symlink rather than copy
    @param      system_site_packages    Give the virtual environment access to the system site-packages dir
    @param      clear                   Delete the environment directory if it already exists.
                                        If not specified and the directory exists, an error is raised.
    @param      packages                list of packages to install (it will install module
                                        `pymyinstall <>`_).
    @param      fLOG                    logging function
    @param      temp_folder             temporary folder (to download module if needed), by default ``<where>/download``
    @return                             stand output

    @example(Create a virtual environment)
    The following example creates a virtual environment.
    Packages can be added by specifying the parameter *package*.

    @code
    from pyquickhelper.pycode import create_virtual_env
    fold = "my_env"
    if not os.path.exists(fold):
        os.mkdir(fold)
    create_virtual_env(fold)
    @endcode

    @endexample
    """
    fLOG("create virtual environment at:", where)
    params = {}
    if symlinks:
        params["symlinks"] = None
    if system_site_packages:
        params["system-site-packages"] = None
    if clear:
        params["clear"] = None
    cmd = build_venv_cmd(params, [where])
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
    if len(err) > 0:
        raise VirtualEnvError(
            "unable to create virtual environement at {2}\nCMD:\n{3}\nOUT:\n{0}\nERR:\n{1}".format(out, err, where, cmd))
            
    scripts = os.path.join(where, "Scripts")
    if not os.path.exists(scripts):
        files = "\n  ".join(os.listdir(where))
        raise FileNotFoundError("unable to find {0}, content:\n  {1}".format(scripts, files))

    if packages is not None and len(packages) > 0:
        fLOG("install packages in:", where)
        if "pymyinstall" in packages:
            packages = [_ for _ in packages if _ != "pymyinstall"]
        out += venv_install(where, packages, fLOG=fLOG,
                            temp_folder=temp_folder)
    return out


def venv_install(venv, packages, fLOG=print, temp_folder=None):
    """
    install a package or a list of packages in a virtual environment

    @param      venv            location of the virtual environment
    @param      packages        a package (str) or a list of packages(list[str])
    @param      fLOG            logging function
    @param      temp_folder     temporary folder (to download module if needed), by default ``<where>/download``
    @return                     standard output
    """
    if temp_folder is None:
        temp_folder = os.path.join(venv, "download")

    if isinstance(packages, str):
        packages = [packages]

    p = os.path.normpath(os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "..", ".."))
    l = ','.join("'{0}'".format(_) for _ in packages)
    script = ["import sys",
              "sys.path.append('{0}')".format(p.replace("\\", "\\\\")),
              "import pymyinstall",
              "ps=[{0}]".format(l),
              "t='{0}'".format(temp_folder.replace("\\", "\\\\")),
              "pymyinstall.packaged.install_all(temp_folder=t,list_module=ps)"]
    return run_venv_script(venv, "\n".join(script), fLOG=fLOG)


def run_venv_script(venv, script, fLOG=print, file=False):
    """
    run a script on a vritual environment (the script should be simple

    @param      venv        virtual environment
    @param      script      script as a string (not a file)
    @param      fLOG        logging function
    @param      file        is script a file or a string to execute
    @return                 output
    """
    script = ";".join(script.split("\n"))
    exe = os.path.join(venv, "Scripts", "python")
    if file:
        if not os.path.exists(script):
            raise FileNotFoundError(script)
        cmd = " ".join([exe, "-u", '"{0}"'.format(script)])
    else:
        cmd = " ".join([exe, "-u", "-c", '"{0}"'.format(script)])
    out, err = run_cmd(cmd, wait=True, fLOG=fLOG)
    if len(err) > 0:
        raise VirtualEnvError(
            "unable to run script at {2}\nCMD:\n{3}\nOUT:\n{0}\nERR:\n{1}".format(out, err, venv, cmd))
    return out
