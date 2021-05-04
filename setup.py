#!/usr/bin/env python

import os
from setuptools import setup

scripts = ["rexmenu.py"]
if os.path.exists("/usr/bin/tvservice"):
    scripts.append("scripts/rpi-screen-blank.py")

with open("README.rst", "r") as fp:
    long_description = fp.read()

setup(name='rexmenu',
      version='2.0',
      description='Simple image tiling program launcher/MAME frontend using Pygame',
      long_description=long_description,
      author='Rob McMullen',
      author_email='feedback@playermissile.com',
      url='https://playermissile.com',
      scripts=scripts,
      license="MPL 2.0",
      install_requires = [
          'pygame',
          ],
     )
