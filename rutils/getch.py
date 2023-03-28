import sys
import tty
import termios

def getch():
    """
    Read a single character from the user.
    """
    # Save the terminal settings.
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        # Set the terminal settings to raw mode.
        tty.setraw(sys.stdin.fileno())

        # Read a single character from the user.
        ch = sys.stdin.read(1)
    finally:
        # Restore the terminal settings.
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return ch
