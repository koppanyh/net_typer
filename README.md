# net_typer

A little utility to control the keyboard through a socket

## Setup

- On the target computer, start the script with `python3 net_typer.py`
- On the controller computer, use `netcat` (or any other raw socket program) to initiate a connection to `<target computer IP>:20052`
  - Example: `nc localhost 20052`
- You'll know the connection is successful when you see `N3T TYP3R (c)22 v0.9` show up on the controller computer

## How it works

You send a string of whatever you want to be typed on the target computer.\
E.g. sending `hello world` will type `hello world` on the target computer.\
Strings must be terminated by a newline.

There is support for sending hotkey combinations by encapsulating them in square brackets.\
E.g. sending `[alt tab]hello world` will press Alt+Tab (to switch to another window) and then type `hello world`.\
A list of the allowed keys are listed [here](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys).\
Pro tip: if the hotkey is the thing, the `]` can be omitted.\
E.g. sending `hello world[enter` will type `hello world` and then press enter.

Hotkeys can be added in multiple places.\
E.g. sending `type in window 1[alt tab]type in window 2[enter]` will type in the first window, then switch to the 2nd window and type in that, then it will press enter in the 2nd window.

If you want to type an opening square bracket character without it being interpreted as a hotkey, prefix it with a backslash.\
E.g. sending `hello \[world` will type `hello [world`.

If you want to exit, send the hotkey `[exit]`.\
This can also be mixed with other text before the exit hotkey.

## Dependencies

- [Python 3](https://www.python.org/downloads/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)
