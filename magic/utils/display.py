from sys import stdout


class Colors:
    BLACK = "\u001b[30m"
    RED = "\u001b[31m"
    GREEN = "\u001b[32m"
    YELLOW = "\u001b[33m"
    BLUE = "\u001b[34m"
    MAGENTA = "\u001b[35m"
    CYAN = "\u001b[36m"
    WHITE = "\u001b[37m"
    RESET = "\u001b[0m"


def in_color(text, color):
    return f'{color}{text}{Colors.RESET}'


def print_error(error):
    print(f"""{Colors.RED}🔥 {error}{Colors.RESET}""")


def clear_last_line():
    stdout.write("\033[F")  # back to previous line
    stdout.write("\033[K")  # clear line
