"""
@brief      test log(time=1290s)

skip this test for regular run
"""

import sys
import os
import unittest


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    if "PYQUICKHELPER" in os.environ and len(os.environ["PYQUICKHELPER"]) > 0:
        sys.path.append(os.environ["PYQUICKHELPER"])
    import pyquickhelper as skip_


from src.pymyinstall.installcustom import install_python
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


class TestDownloadPythonPyQuickHelper (unittest.TestCase):

    def test_install_python_pyquickhelper(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        vers = "%d%d" % sys.version_info[:2]
        temp = get_temp_folder(
            __file__, "temp_python%s_pyquickhelper" % vers, clean=False)

        if sys.platform.startswith("win"):
            install_python(install=True, temp_folder=temp,
                           fLOG=fLOG, modules="pyquickhelper", custom=True, latest=True)
            pyt = os.path.join(temp, "python.exe")
            pip = os.path.join(temp, "Scripts", "pip.exe")
            if not os.path.exists(pyt):
                raise FileNotFoundError(pyt)
            if not os.path.exists(pip):
                raise FileNotFoundError(pip)


if __name__ == "__main__":
    unittest.main()
