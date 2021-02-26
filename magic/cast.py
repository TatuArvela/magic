from os import system, WEXITSTATUS
from string import Template

from magic.utils.display import Colors, in_color, print_error
from magic.utils.spellbook import get_spells


def check_args(argument_count, spell_args):
    if argument_count is not None and len(spell_args) < argument_count:
        raise Exception(f'Not enough arguments, {argument_count} required')
    return spell_args


def substitute_args(text, args):
    template = Template(text)
    args_dict = {f'a{index}': arg for index, arg in enumerate(args)}
    return template.substitute(**args_dict)


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
            spell_args = check_args(spell.get('argumentCount'), spell_args)
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
