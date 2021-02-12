import sys


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


def create_prompt(color=Colors.WHITE, multiline=False):
    def prompt_input(validate, default):
        input_message = ""
        if default is not None:
            input_message = f"(default: {default}) "

        response = None
        while response is None:
            response = input(input_message)
            if default is not None:
                if response == "":
                    response = default
            if validate is not None:
                if validate(response) is False:
                    response = None
                    clear_response_line()

        return response

    def prompt(message, validate=None, default=None):
        print(in_color(message, color))
        if multiline:
            lines = []
            while True:
                line = prompt_input(validate, default)
                if line:
                    lines.append(line)
                else:
                    clear_response_line()
                    break
            return lines
        else:
            return prompt_input(validate, default)
    return prompt


def validate_required(line):
    return line != ""


def validate_number(line):
    return line.isnumeric()


def validate_yes_no(line):
    return line.lower() == 'y' or line.lower() == 'n'


def clear_response_line():
    sys.stdout.write("\033[F")  # back to previous line
    sys.stdout.write("\033[K")  # clear line
