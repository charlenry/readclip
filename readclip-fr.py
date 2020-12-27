#!/usr/bin/env python3
#
# QU'EST-CE QUE READCLIP ?
# Ce script, quand il est lancé, permet de lire à haute voix un texte en français qui a été copié dans le presse-papier.
# Ce qui est lu est également enregistré dans un fichier out.wav dans le même dossier que le script.
# Le contenu du fichier out.wav change à chaque nouvelle copie dans le presse-papier.
# Ce script est destiné au système Linux qui manque de ce type d'application.
# Ce script utilise le moteur TTS Pico SVOX.
# Ce script a été testé sous Linux Ubuntu 14.04 LTS.
#
# PRÉREQUIS :
# Pour que le script fonctionne, il faut installer les paquets libttspico-utils, libttspico0, libttspico-data, sox, libsox-fmt-alsa, libsox-fmt-base, libsox2 et xsel.
# Accessoirement, vous pouvez installer les paquets mbrola et espeak avec les langues de votre choix.
#
# USAGE :
# Tapez la ligne de commande suivante dans un terminal où se trouve le script :
# $ ./readclip-fr.py
# Puis sélectionnez et copiez le texte en français de votre choix pour entendre la lecture du texte. 
# Tant que le script fonctionne, tout texte copié dans le presse-papier sera lu.
# Pour arrêter la lecture du presse-papier, appuyez sur les touches "Ctrl + C" dans le terminal pour arrêter le script.


import gi, os
lang = 'fr-FR'

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def callback(*args):
# print(clip.wait_for_text(), flush=True)
	buffering = clip.wait_for_text()
	text = buffering.replace('"',"")
	os.system('pico2wave -l %s -w out.wav "%s"' % (lang,text))
	os.system('play out.wav speed 0.95 treble +14')

clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect('owner-change', callback)
Gtk.main()
