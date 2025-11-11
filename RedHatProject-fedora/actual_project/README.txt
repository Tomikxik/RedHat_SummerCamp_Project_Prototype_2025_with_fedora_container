welcome to our game Wizard cooking
made by Tomikxik, Nikol

Builded in python 3.12 and tested in 3.11/12/13
App resolution is 1200 x 960 because we dont have pixel arts with Big resolution

Requirements:
	Functional PC :)
	Following instructions below

1. install python 3.13.5 or at least some 3.			(builded in 3.12(64-bit))
	Go to the official site: https://www.python.org/downloads/
	Click the download link for Python 3.13.5 (or the latest 3.x).
	Run the installer:
		Check “Add Python to PATH” at the start.
		Make sure tcl/tk and IDLE is selected (for Tkinter).

1.5. install python tkinter(if not installed with python)
	
	start up cmd/terminal

	Windows:
	#should download with python

	Linux:
		Debian/Ubuntu:
			:sudo apt install python3-tk
		Fedora:
			:sudo dnf install python3-tkinter
		Arch:
			:sudo pacman -S tk
	macOS:
	:brew install python-tk


2. install (PIL) pillow library by pip(i hope you have pip)

	Windows:
	: pip install Pillow

	Linux/macOS
	: pip3 install Pillow

3. Check if the Python, tkinter and PIL download correctly *

	Windows:
	*console check:
	:python
	>>> from PIL import Image, ImageTk
	*if here is no answer or error everything is working

	Linux/macOS:
	*console check:
	:python3
	>>> from PIL import Image, ImageTk
	*if here is no answer or error everything is working

4. run RUNME.py

	Windows:
	:python RUNME.py
	
	Linux/macOS:
	:python3 RUNME.py


*Linux only

*You need to disable linux su - setenforce 0 to gain container access to /tmp/.X11-unix \
*If it isnt downloaded correctly u can try to use my docker with bash file to create system container and try to run it there
*The libraries and other setup is included

	./run.sh


any game tips and other game instructions are located in instruction game button

Have FUN!!!		:)

