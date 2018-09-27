# stick_hero_game_solver
Plays the android game 'Ninja Stick Hero' automically and infinitely, without dying...

## requirements
*this repository also contains the required adb tools for the project*
1. You need to enable developer options on your android device.
2. You need to enable 'usb debugging' in the developers options, and allow unknown devices to act as input source and control scteen touch input.
3. when you clone this repository, add this folder to "enviornment variables->paths" in your pc.(to identify and run adb commands)
4. you need to have all the essential python libraries installed, and python 3.4 preferably. 'Jupyter notebook' is not essential but i used it to compile python, so those *.ipynb* files are present.

## working

The code extracts the screen from your android device using *Adb*, processes the image, and then calculates the length of press for the ideal length of the stick.
Then it access the screen using the Android-Debug-Bridge(*Adb*), and gives a tap input of ideal length for the solving of game.
