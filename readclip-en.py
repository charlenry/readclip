#!/usr/bin/env python3
#
# WHAT IS READCLIP?
# This script, when launched, allows you to read aloud a text in English which has been copied to the clipboard.
# What is played is also saved in an out.wav file in the same folder as the script.
# The contents of the out.wav file change with each new copy to the clipboard.
# This script is intended for the Linux system which lacks this type of application.
# This script uses the TTS Pico SVOX engine.
# This script has been tested on Linux Ubuntu 14.04 LTS and Linux Mint 20.1.
#
# PREREQUISITES:
# For the script to work, install the libttspico-utils, libttspico0, libttspico-data, sox, libsox-fmt-alsa, libsox-fmt-base, libsox2 (or libsox3 for Linux Mint 20.1) and xsel packages.
#
# USAGE:
# Type the following command line into a terminal where the script is located:
# $ ./readclip-en.py
# Then select and copy the English text of your choice to hear the text read.
# As long as the script is running, any text copied to the clipboard will be read.
# To stop clipboard playback, press the "Ctrl + C" keys in the terminal to stop the script.


import gi, os
lang = 'en-GB'

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def callback(*args):
# print(clip.wait_for_text(), flush=True)
	buffering = clip.wait_for_text()
	text = buffering.replace('"',"")
	os.system('pico2wave -l %s -w out.wav "%s"' % (lang,text))
	os.system('play out.wav speed 0.86 treble +30')

clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect('owner-change', callback)
Gtk.main()
