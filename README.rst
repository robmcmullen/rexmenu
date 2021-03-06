============================
RexMenu
============================

A simple image-tiling program launcher, designed primarily as frontend for MAME but easily supporting other emulators.

.. image:: https://playermissile.com/_images/rexmenu_screenshot.png
   :align: center

.. contents:: **Contents**

Prerequisites
=============

* Python 2.7
* pygame
* python-evdev (optional, for screen blanking utility on Raspberry Pi)

Pygame has recently become installable through pip if the correct dependencies
are installed. On linux it is probably available through your package manager.
It is installed by default in the RetroPie distribution for the Raspberry Pi.
Binaries are also available at the `Pygame website
<http://www.pygame.org/wiki/GettingStarted>`_.

Limitations
===========

RexMenu does not perform any discovery of ROMs or any scraping to get metadata.
Any images used have to be sourced outside this program.

Install
=======

Install with::

    pip install rexmenu

Usage
=====

The program may be started from the command line, or autostarted by some means
depending on your operating system. Either way, if you have installed rexmenu
through pip, the script will be in your search path and can be started simply
by::

    rexmenu.py

RexMenu takes no command line arguments; it needs a configuration file that
lists all of the emulators and games. An example file is in the source
distribution as ``rexmenu.cfg.sample``. See the Configuration section below for
more details.

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
provides many emulators. Its default frontend was too complicated for my small
kids to use, so I designed this based on some code from a listener (I host the
`Player/Missile Podcast <https://playermissile.com>`_) Rex. And hence the name.

In RetroPie, you can autostart RexMenu by editing the file::

    /opt/retropie/configs/all/autostart.sh

Extras
------

For the RaspberryPi, I have included some extras. The program ``rpi-screen-blank.py``
will turn off the monitor after a set amount of time (default of 10
minutes) where it doesn't detect any keyboard or mouse input. It works by using
the Python evdev module to monitor keyboard events and uses some RaspberryPi-
specific commands to blank the console screen, which enables the DPMS of the
monitor, putting it into low power standby mode.

Configuration
=============

The RexMenu configuration file tis in INI-style format, with one required
section that sets some application options, and any number of other sections
describing the available programs to launch.  Here is an example of a
configuration file::

    [rexmenu]
    title = title.png
    quit = ESCAPE
    image path = /home/pi/src/arcade-screenshots
    thumbnail size = 250
    windowed = False
    window width = 1280
    window height = 1024
    highlight size = 8

    [advmame]
    digdug = Dig Dug
    mappy = Mappy
    mpatrol = Moon Patrol
    flicky = Flicky
    pacmania = Pac-Mania
    pacman = Pac-Man
    mspacman = Ms. Pac-Man
    nrallyx = Rally X
    berzerk = Berzerk

    [atari800 -xl -pal]
    /share/atari/yoomp.atr = Yoomp!

    [python]
    image path = /share/rex
    /share/rex/atari/combat.py = Combat

The configuration file can be stored as ``.rexmenu`` in your home directory, or
as ``rexmenu.cfg`` in the same directory as the ``rexmenu.py`` program.

rexmenu Section
---------------

The ``rexmenu`` section defines the appearance and control of the launcher.

Keystroke Options
~~~~~~~~~~~~~~~~~

The configuration options for keystrokes are::

    run
    quit
    up
    down
    left
    right
    konami_a
    konami_b

where each of those takes a text list of `pygame keyboard identifiers
<https://www.pygame.org/docs/ref/key.html>`_ without the leading ``K_``. For
example, the default set of controls for ``run`` is::

    [rexmenu]
    run = Z X LSHIFT LCTRL SPACE RETURN 1 2 3 4

The Konami code is available (up up down down left right left right B A) for a
function, currently to exit the frontend, but in the future will be user-
defined.  The ``konami_a`` and ``konami_b`` config items are available to set
what the program will use for the B and A keys, defaulting to ``2`` and ``1``
respectively.

Image Options
~~~~~~~~~~~~~

* ``image path`` *(space separated list)* list of paths to search for images if
  the image isn't found in emulator-specific image paths. If a path has spaces
  within it, enclose the path in single or double quotes.
* ``thumbnail size`` *(int)* images will be resized to fit within the square with each side being this size in pixels

Other Options
~~~~~~~~~~~~~

* ``title`` *(string)* path to an optional title graphic displayed at the top of the screen
* ``windowed`` *(boolean)* if True, use window instead of full screen
* ``window width`` *(int)* height of window in pixels if in windowed mode
* ``window height`` *(int)* width of window in pixels if in windowed mode
* ``highlight size`` *(int)* width in pixels of the line used to draw the highlight box
* ``grid spacing`` *(int)* number of pixels padding between grid entries
* ``name spacing`` *(int)* number of pixels padding between grid image and text showing the name of the game
* ``clear screen`` *(boolean)* whether or not to clear the console screen before displaying the menu
* ``wrap menu`` *(boolean)* allow the cursor to wrap to the top or bottom when attempting to move beyond the bottom or top
* ``konami code`` *(string)* action to perform when the Konami code is completed (see the `Konami Code`_ section below)

Other Sections
--------------

The remaining sections of the config file describe a command line used to
launch the emulator, and the list of filenames of games that use that emulator.
Any number of sections may be included in the config file, and the program will
display all games in alphabetical order regardless of which section of the
config file they appear.

The section name is the path and command line arguments to the emulator that
will run all the entries in that section. Entries for the same emulator but
using different command line options are possible.  For instance, to use the
`atari800 <http://atari800.sourceforge.net/>`_ emulator in NTSC (60 Hz display)
for some games and PAL (50 Hz display) for others, two sections could be
added::

    [atari800]
    /opt/games/atari8bit/Jumpman.atr = Jumpman

    [atari800 -pal]
    /opt/games/atari8bit/Jumpman.atr = Jumpman (PAL)

This is the format of entries: the key (the left hand side, before the ``=``)
which is the path to the ROM file, and the value (the right hand side, after
the ``=``) which is the name of the game to display in the grid.

If the title is the same name as the filename, you can use the entry "title
from name" and just list the paths to the games separated by whitespace (the
directory portion and the file extension will be removed for display)::

    [atari800]
    title from name = /opt/games/atari8bit/Jumpman.atr /opt/games/atari8bit/Livewire.xex

If the emulator program is not in the search path, you can use the full path to
the emulator as the section title::

    [/opt/games/bin/atari800 -xl]
    /opt/games/atari8bit/yoomp.atr = Yoomp!

Images
------

Images for the grid are loaded based on the filename of the game, not the text
title. PNG and JPEG files are supported. The path is stripped off of the game
and the extension ".png" or ".jpg" is added to both the whole filename and the
filename stripped of its extension. The first one found is used. So for
``/opt/games/atari8bit/Jumpman.atr``, the names::

    Jumpman.atr.png
    Jumpman.atr.jpg
    Jumpman.png
    Jumpman.jpg

are searched for in that order.

They are searched for in the same directory as the game, or in one of the paths
specified by the ``image path`` item in either in the individual emulator
section, or the ``rexmenu`` section. The path specified in the emulator
sections will be searched before the paths in the ``rexmenu`` section.

Note again that RexMenu has no metadata scraping, so you'll have to download or
create the images yourself. For MAME, a relatively complete set of screenshot images can be found at::

    http://www.progettosnaps.net/snapshots/

Konami Code
-----------

When the Konami code is completed, RexMenu will perform the action defined in
the ``konami code`` entry in the main configuration section.  Currently, there
are two types of actions:

* ``exit``: exit the menu, back to the command line
* *config file name*: load an alternate configuration file and display that menu.

When the alternate configuration file is used, it can have its own Konami code
action, so you can chain menus in this manner.

License
=======

RexMenu, the MAME frontend sponsored by the Player/Missile Podcast
Copyright (c) 2016-2017 Rob McMullen (feedback@playermissile.com)

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
