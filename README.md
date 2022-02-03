## What is ReadClip? ##
This script, when launched, allows you to read aloud a text in English or French or Spanish which has been copied to the clipboard.
What is played is also saved in an `out.wav` file in the same folder as the script.
The contents of the `out.wav` file change with each new copy to the clipboard.
This script is intended for the Linux system which lacks this type of application.
It uses the TTS Pico SVOX engine.
It has been tested on Linux Ubuntu 14.04 LTS and Linux Mint 20.1.

## Prerequisites: ##
For the script to work, install the `libttspico-utils`, `libttspico0`, `libttspico-data`, `sox`, `libsox-fmt-alsa`, `libsox-fmt-base`, `libsox2` (or `libsox3` for Linux Mint 20.1) and `xsel` packages.

## Usage: ##
Type the following command line into a terminal where the script is located depending on the text language you want to read:

	For English texts:
		$ ./readclip-en.py
		
	For French texts:
		$ ./readclip-fr.py
		
	For Spanish texts:
		$ ./readclip-es.py

Then select and copy the text of your choice to hear the text read.
As long as the script is running, any text copied to the clipboard will be read.
To stop clipboard playback, press the `Ctrl + C` keys in the terminal to stop the script.

Other languages are possible. Available languages: US English: `en-US`, UK English: `en-GB`, German: `de-DE`, Spanish: `es-ES`, French: `fr-FR`, Italian: `it-IT`. You just have to change the value of the `lang` variable.
