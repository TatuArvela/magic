import sys

from magic.shared.display import Color, clear_last_line, in_color
from magic.shared.validation import is_yes_or_no


def prompt(
    message,
    color=Color.WHITE,
    multiline=False,
    validate=None,
    default=None,
    required=False,
    yes_or_no=False,
):
    print(in_color(message, color))

    if multiline:
        lines = []
        while True:
            line = __prompt_input(validate, default)
            if line:
                lines.append(line)
            elif not required or len(lines) > 0:
                clear_last_line()
                break
        return lines

    if yes_or_no:
        return __yes_or_no(__prompt_input(is_yes_or_no, default, required))

    return __prompt_input(validate, default, required)


def __prompt_input(validate=None, default=None, required=False):
    input_message = "> "

    response = None
    while response is None:
        try:
            response = input(in_color(input_message, Color.CYAN))
        except KeyboardInterrupt:
            sys.exit()

        if default is not None:
            if response == "":
                clear_last_line()
                print(in_color(f"{input_message}{default}", Color.CYAN))
                response = default

        if required and response == "":
            response = None
            clear_last_line()

        if validate is not None:
            if validate(response) is False:
                response = None
                clear_last_line()

    return response


def __yes_or_no(value):
    if value == "y" or value == "yes":
        return True
    return False
