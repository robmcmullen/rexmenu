#!/usr/bin/env python

import os
from distutils.core import setup

scripts = ["rexmenu.py"]
if os.path.exists("/usr/bin/tvservice"):
    scripts.append("scripts/rpi-screen-blank.py")

with open("README.rst", "r") as fp:
    long_description = fp.read()
print long_description

setup(name='rexmenu',
      version='2.0',
      description='Simple image tiling program launcher/MAME frontend using Pygame',
      long_description=long_description,
      author='Rob McMullen',
      author_email='feedback@playermissile.com',
      url='https://playermissile.com',
      scripts=scripts,
      license="GPL",
      install_requires = [
          'pygame',
          ],
     )
