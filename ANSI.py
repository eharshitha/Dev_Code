# ansi.py
# Reusable Python ANSI Escape Code Library

# ==========================================
# RESET
# ==========================================

reset = "\033[0m"
reset_all = "\033[0m"

reset_bold = "\033[22m"
reset_italic = "\033[23m"
reset_underline = "\033[24m"
reset_blink = "\033[25m"
reset_reverse = "\033[27m"
reset_hidden = "\033[28m"
reset_strikethrough = "\033[29m"
reset_fg = "\033[39m"
reset_bg = "\033[49m"


# ==========================================
# TEXT FORMATTING
# ==========================================

bold = "\033[1m"
dim = "\033[2m"
italic = "\033[3m"
underline = "\033[4m"
slow_blink = "\033[5m"
rapid_blink = "\033[6m"
reverse = "\033[7m"
hidden = "\033[8m"
strikethrough = "\033[9m"


# ==========================================
# STANDARD FOREGROUND COLORS
# ==========================================

black = "\033[30m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
white = "\033[37m"


# ==========================================
# BRIGHT FOREGROUND COLORS
# ==========================================

bright_black = "\033[90m"
bright_red = "\033[91m"
bright_green = "\033[92m"
bright_yellow = "\033[93m"
bright_blue = "\033[94m"
bright_magenta = "\033[95m"
bright_cyan = "\033[96m"
bright_white = "\033[97m"


# ==========================================
# STANDARD BACKGROUND COLORS
# ==========================================

bg_black = "\033[40m"
bg_red = "\033[41m"
bg_green = "\033[42m"
bg_yellow = "\033[43m"
bg_blue = "\033[44m"
bg_magenta = "\033[45m"
bg_cyan = "\033[46m"
bg_white = "\033[47m"


# ==========================================
# BRIGHT BACKGROUND COLORS
# ==========================================

bg_bright_black = "\033[100m"
bg_bright_red = "\033[101m"
bg_bright_green = "\033[102m"
bg_bright_yellow = "\033[103m"
bg_bright_blue = "\033[104m"
bg_bright_magenta = "\033[105m"
bg_bright_cyan = "\033[106m"
bg_bright_white = "\033[107m"


# ==========================================
# 256 COLORS
# ==========================================

def fg(n):
    """Return a 256-color foreground escape code."""
    if not 0 <= n <= 255:
        raise ValueError("Color must be between 0 and 255")
    return f"\033[38;5;{n}m"


def bg(n):
    """Return a 256-color background escape code."""
    if not 0 <= n <= 255:
        raise ValueError("Color must be between 0 and 255")
    return f"\033[48;5;{n}m"


# ==========================================
# RGB TRUE COLORS
# ==========================================

def rgb(r, g, b):
    """Return an RGB foreground escape code."""
    if not all(0 <= v <= 255 for v in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    return f"\033[38;2;{r};{g};{b}m"


def bg_rgb(r, g, b):
    """Return an RGB background escape code."""
    if not all(0 <= v <= 255 for v in (r, g, b)):
        raise ValueError("RGB values must be between 0 and 255")
    return f"\033[48;2;{r};{g};{b}m"


# ==========================================
# CURSOR MOVEMENT
# ==========================================

def move_up(n=1):
    return f"\033[{n}A"


def move_down(n=1):
    return f"\033[{n}B"


def move_right(n=1):
    return f"\033[{n}C"


def move_left(n=1):
    return f"\033[{n}D"


def column(n):
    return f"\033[{n}G"


def position(row, col):
    return f"\033[{row};{col}H"


# ==========================================
# SCREEN AND LINE CLEARING
# ==========================================

clear_screen = "\033[2J"
clear_to_end_screen = "\033[0J"
clear_from_start_screen = "\033[1J"

clear_line = "\033[2K"
clear_to_end_line = "\033[0K"
clear_from_start_line = "\033[1K"


# ==========================================
# CURSOR VISIBILITY
# ==========================================

show_cursor = "\033[?25h"
hide_cursor = "\033[?25l"


# ==========================================
# HELPER FUNCTIONS
# ==========================================

def color(text, foreground=None, background=None):
    """Apply foreground and background colors to text."""
    start = ""
    if foreground is not None:
        start += foreground
    if background is not None:
        start += background
    return f"{start}{text}{reset}"


def styled(text, *styles):
    """Combine multiple ANSI styles."""
    return f"{''.join(styles)}{text}{reset}"


def print_color(text, foreground=None, background=None, end="\n"):
    """Print text with optional foreground and background colors."""
    print(color(text, foreground, background), end=end)


def print_styled(text, *styles, end="\n"):
    """Print text with multiple ANSI styles."""
    print(styled(text, *styles), end=end)
