============================
RexMenu
============================

A simple image-tiling multipurpose program launcher, designed primarily as frontend for MAME but easily supporting other emulators.

Prerequisites
=============

* Python 2.7
* pygame

In addition, RexMenu does not perform any discovery of ROMs or any scraping to
get metadata. Any images used have to be sourced outside this program.

Install
=======

Install with::

    pip install rexmenu

Configuration
=============

RexMenu needs a configuration file that lists all of the emulators and games.
It is in INI-style format, with one required section that sets some application
options, and any number of other sections describing the available programs to
launch.

The configuration file can be stored as `.rexmenu` in your home directory, or
as `rexmenu.cfg` in the same directory as the `rexmenu.py` program.

An example file is in the source distribution as rexmenu.cfg.sample.

Usage
=====

The program may be launched from the command line, or autostarted by some means
depending on your operating system. Either way, it is started simply by::

    python path/to/rexmenu.py

Raspberry Pi
============

RexMenu works well on the Raspberry Pi because pygame works on the console
graphics. You do not need to have X running.

RetroPie
--------

I have two MAME cabinets running the `RetroPie <https://retropie.org.uk/>`_
distribution on `Raspberry Pi 3 <https://raspberrypi.org>`_. It is a Raspbian-
based linux distribution that preloads several emulators and a default front
end that was too complicated for my small kids to use, so I designed this based
on some code from a listener, Rex (hence the name), to my `Player/Missile
Podcast <https://playermissile.com>`_.

