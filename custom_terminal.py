import os
import platform
import sys

def set_terminal_title(title):
    """Set the terminal title based on the operating system."""
    system = platform.system()
    if system == "Windows":
        os.system(f'title {title}')
    elif system in ["Linux", "Darwin"]:  # macOS is Darwin
        print(f"\033]0;{title}\a", end='')

def set_terminal_color_scheme():
    """Set terminal color scheme based on the operating system."""
    system = platform.system()
    if system == "Windows":
        os.system('color 0A')  # Set green text on black background
    elif system == "Linux":
        os.system('setterm -term linux -back black -fore green')  # Set green text on black background
    elif system == "Darwin":  # macOS
        os.system('printf "\033[1;32m"')  # Set green text

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

if __name__ == "__main__":
    # Example usage
    clear_terminal()
    set_terminal_title("Cyber Hub DDoS Tool")
    set_terminal_color_scheme()
    print("Welcome to the Cyber Hub DDoS Tool!")
