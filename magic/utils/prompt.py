from magic.utils.display import Colors, in_color, clear_last_line


def create_prompt(color=Colors.WHITE, multiline=False):
    def prompt(message, validate=None, default=None):
        print(in_color(message, color))
        if multiline:
            lines = []
            while True:
                line = prompt_input(validate, default)
                if line:
                    lines.append(line)
                else:
                    clear_last_line()
                    break
            return lines
        else:
            return prompt_input(validate, default)

    return prompt


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
                clear_last_line()

    return response
