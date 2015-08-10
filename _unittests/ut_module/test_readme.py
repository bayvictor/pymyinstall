"""
@brief      test tree node (time=50s)
"""

import sys
import os
import unittest
import re
import shutil
import warnings
import pandas

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
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder
from src.pymyinstall.installhelper.install_venv_helper import create_virtual_env, run_venv_script


class TestReadme(unittest.TestCase):

    def test_venv_docutils08_readme(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fold = os.path.dirname(os.path.abspath(__file__))
        readme = os.path.join(fold, "..", "..", "README.rst")
        assert os.path.exists(readme)
        with open(readme, "r", encoding="utf8") as f:
            content = f.read()

        temp = get_temp_folder(__file__, "temp_readme")
        out = create_virtual_env(temp, fLOG=fLOG, packages=["docutils==0.8"])
        outfile = os.path.join(temp, "conv_readme.html")

        script = ["from docutils import core",
                  "settings_overrides = {'output_encoding': 'unicode', 'doctitle_xform': True, 'initial_header_level': 2, 'warning_stream': io.StringIO()}",
                  "parts = core.publish_parts(source=s, source_path=None, destination_path=None, writer_name='html', settings_overrides=settings_overrides)",
                  "with open('{0}', 'w', encoding='utf8') as f:".format(
                      outfile),
                  "    f.write(parts['whole']",
                  ]

        out = run_venv_script(temp, "\n".join(script), fLOG=fLOG)


if __name__ == "__main__":
    unittest.main()
