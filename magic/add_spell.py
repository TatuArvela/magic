from .utils import Colors, in_color, create_prompt, validate_yes_no, validate_number, validate_required

color = Colors.CYAN
prompt = create_prompt(color)
multiline_prompt = create_prompt(color, multiline=True)
step_index = 0


def step():
    global step_index
    step_index += 1
    return step_index


def add_spell():
    print(f'{in_color("🧙 Adding a new spell to your spellbook", color)}')

    description = prompt(f'{step()}. Enter a description. You may use $a0, $a1, etc. to be shown as part of the message.', validate=validate_required)
    magic_words = prompt(f'{step()}. Enter magic words, separated by a comma:', validate=validate_required)
    commands = multiline_prompt(f'{step()}. Enter commands to be run in the spell, separated by line breaks. You may use $a0, $a1, etc. to provide arguments. Leave an empty line to stop.')
    arguments_required = prompt(f'{step()}. Enter the number of arguments required', validate=validate_number, default='0')
    show_message = prompt(f'{step()}. Show message when casting the spell, y or n?', validate=validate_yes_no, default='y')
    show_success_message = prompt(f'{step()}. Show success message, y or n?', validate=validate_yes_no, default='y')

    magic_words = [word.strip(' ') for word in magic_words.split(',')]
    show_message = show_message == 'y'
    show_success_message = show_success_message == 'y'

    spell = {
        "description": description,
        "magicWords": ",".join(magic_words),
        "commands": ",".join(commands),
        "argumentsRequired": arguments_required,
        "showMessage": show_message,
        "showSuccessMessage": show_success_message
    }

    print(spell)
