#!/usr/bin/env python3
# ¿QUÉ ES READCLIP?
# Este script, cuando se inicia, le permite leer en voz alta un texto en español que se ha copiado al portapapeles.
# Lo que se reproduce también se guarda en un archivo out.wav en la misma carpeta que el script.
# El contenido del archivo out.wav cambia con cada nueva copia al portapapeles.
# Este script está destinado al sistema Linux que carece de este tipo de aplicación.
# Este script utiliza el motor TTS Pico SVOX.
# Este script ha sido probado en Linux Ubuntu 14.04 LTS.
#
# PRERREQUISITOS:
# Para que el script funcione, instale los paquetes libttspico-utils, libttspico0, libttspico-data, sox, libsox-fmt-alsa, libsox-fmt-base, libsox2 y xsel.
# Por cierto, puede instalar los paquetes mbrola y espeak con los idiomas que elija.
#
# UTILIZACIÓN:
# Escriba la siguiente línea de comando en una terminal donde se encuentra el script:
# $ ./readclip-es.py
# Luego seleccione y copie el texto en español de su elección para escuchar el texto leído.
# Mientras se esté ejecutando el script, se leerá cualquier texto copiado en el portapapeles.
# Para detener la reproducción del portapapeles, presione las teclas "Ctrl + C" en la terminal para detener el script.


import gi, os
lang = 'es-ES'

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

def callback(*args):
# print(clip.wait_for_text(), flush=True)
	buffering = clip.wait_for_text()
	text = buffering.replace('"',"")
	os.system('pico2wave -l %s -w out.wav "%s"' % (lang,text))
	os.system('play out.wav speed 0.90 treble +14')

clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
clip.connect('owner-change', callback)
Gtk.main()
