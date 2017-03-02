#!/usr/bin/env python

import os
from distutils.core import setup

scripts = ["rexmenu.py"]
if os.path.exists("/usr/bin/tvservice"):
    scripts.append("scripts/rpi-screen-blank.py")

setup(name='rexmenu',
      version='2.0',
      description='Simple frontend for MAME',
      author='Rob McMullen',
      author_email='feedback@playermissile.com',
      url='https://playermissile.com',
      scripts=scripts,
     )
