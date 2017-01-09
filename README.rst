============================
RexMenu
============================

A simple image-tiling multipurpose program launcher, designed primarily as frontend for MAME but easily supporting other emulators.

Prerequisites
=============

* Python 2.7
* pygame
* python-evdev (optional, for screen blanking utility on Raspberry Pi)

In addition, RexMenu does not perform any discovery of ROMs or any scraping to
get metadata. Any images used have to be sourced outside this program.

Install
=======

Install with::

    pip install rexmenu

Usage
=====

The program may be started from the command line, or autostarted by some means
depending on your operating system. Either way, it is started simply by::

    python path/to/rexmenu.py

RexMenu needs a configuration file that lists all of the emulators and games.
An example file is in the source distribution as ``rexmenu.cfg.sample``. See
the Configuration section below for more details.

After starting the program, the display will change to a grid of thumbnail
images with one highlighted. If there are more games defined in the config file
than will fit on screen, up or down arrows will appear indicating that there
are more games in that direction. The joystick or arrow keys can be used to
move the highlight box to different games, and will scroll the list in the
direction of the arrow when you attempt to move the highlight box off the
screen in that direction. Pressing a predefined key will start that game.
Exiting from the game will return you to the RexMenu screen.

Raspberry Pi
============

RexMenu works well on the Raspberry Pi because pygame works on the console
graphics. You do not need to have X running.

RetroPie
--------

The `RetroPie <https://retropie.org.uk/>`_ distribution on `Raspberry Pi 3
<https://raspberrypi.org>`_ is a Raspbian- based linux distribution that
provides many emulators. Its default front was too complicated for my small
kids to use, so I designed this based on some code from a listener, Rex (hence
the name), to my `Player/Missile Podcast <https://playermissile.com>`_.

In RetroPie, you can autostart RexMenu by editing the file::

    /opt/retropie/configs/all/autostart.sh

Extras
------

For the RaspberryPi, I have included some extras. The program ``rpi-screen-
blank.py`` will turn off the monitor after a set amount of time (default of 10
minutes) where it doesn't detect any keyboard or mouse input. It works by using
the Python evdev module to monitor keyboard events and uses some RaspberryPi-
specific commands to blank the console screen, which enables the DPMS of the
monitor, putting it into low power standby mode.

Configuration
=============

The RexMenu configuration file tis in INI-style format, with one required
section that sets some application options, and any number of other sections
describing the available programs to launch.

The configuration file can be stored as ``.rexmenu`` in your home directory, or
as ``rexmenu.cfg`` in the same directory as the ``rexmenu.py`` program.

rexmenu Section
---------------

The ``rexmenu`` section defines the appearance and control of the launcher.  The configuration options for keystrokes are::

    run
    quit
    up
    down
    left
    right
    konami_a
    konami_b

where each of those takes a text list of pygame keyboard identifiers. For example, the default set of controls for ``run`` is::

    [rexmenu]
    run = Z X LSHIFT LCTRL SPACE RETURN 1 2 3 4

The Konami code is available (up up down down left right left right B A) for a
function, currently to exit the emulator, but in the future will be user-
defined.  The ``konami_a`` and ``konami_b`` config items are available to set
what the program will use for the B and A keys, defaulting to ``2`` and ``1``
respectively.

Other options are::

    windowed::

        (True/False) don't use full screen but instead open a window

    int_defaults = {
        "window width": "w",
        "window height": "h",
        "thumbnail size": "thumbnail_size",
        "highlight size": "highlight_size",
        "highlight border": "highlight_border",
        "font border": "font_border",
    }

    bool_defaults = {
        "windowed": "windowed",
        "clear screen": "clear_screen",
    }
