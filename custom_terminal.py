import os
import sys

def set_terminal_title(title):
    if sys.platform == "win32":
        os.system(f'title {title}')
    else:
        print(f"\033]0;{title}\a", end='', flush=True)

def set_terminal_color_scheme():
    os.system('color 0A')  # Set terminal text color to green on black

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
