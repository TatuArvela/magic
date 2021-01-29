from os import system, WEXITSTATUS
from magic.utils import Colors, in_color, print_error
from magic.spellbook import get_spells


def check_args(arguments_expected, spell_args):
    if arguments_expected is not None and len(spell_args) != arguments_expected:
        raise Exception(f'Not enough arguments, {arguments_expected} expected')
    return spell_args


def substitute_args(text, args):
    for idx, arg in enumerate(args):
        text = text.replace('$' + str(idx), arg)
    return text


def handle_message(spell, spell_args):
    description = spell.get("description")
    show_message = spell.get("showMessage")
    if show_message is not False:
        if spell_args is not None:
            description = substitute_args(description, spell_args)
        print(f'✨  {in_color(description, Colors.CYAN)}')


def parse_command(command, spell_args):
    if spell_args is not None:
        command = substitute_args(command, spell_args)
    return command


def cast_spell(arguments):
    try:
        spells = get_spells()
        magic_word = arguments['<spell>']
        spell_args = arguments['<args>']
        spell = spells.get(magic_word)

        if spell:
            spell_args = check_args(spell.get('argumentsExpected'), spell_args)
            handle_message(spell, spell_args)

            executable_commands = ''
            for command in spell['commands']:
                parsed_command = parse_command(command, spell_args)
                executable_commands = f"{executable_commands}\n{parsed_command}"

            exit_code = WEXITSTATUS(system(executable_commands))
            if exit_code != 0:
                raise Exception(f'Command returned exit code {exit_code}')
            return spell.get('showSuccessMessage') is not False

        else:
            raise Exception(f'Spell not found for magic word: {magic_word}')

    except Exception as error:
        print_error(error)
        raise RuntimeError
