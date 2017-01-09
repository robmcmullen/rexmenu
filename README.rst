============================
RexMenu
============================

A simple image-tiling multipurpose program launcher, designed primarily as frontend for MAME but easily supporting other emulators.

Prerequisites
=============

* Python 2.7
* pygame

Install
=======

`pip install rexmenu`

Configuration
=============

RexMenu needs a configuration file that lists all of the emulators and games.
It does not perform any discovery of ROMs or any scraping to get metadata. Any
images used have to be sourced outside this program.

The configuration file is in INI-style format, with one required section that
sets some application options, and any number of other sections describing the
available programs to launch.

The configuration file can be stored as `.rexmenu` in your home directory, or
as `rexmenu.cfg` in the same directory as the `rexmenu.py` program.

An example file is in the source distribution as rexmenu.cfg.sample.

Usage
=====

