from os import system, WEXITSTATUS
from magic.utils import Colors, in_color
from magic.spellbook import open_spellbook


def check_args(arguments_expected, spell_args):
    if arguments_expected is not None:
        if len(spell_args) != arguments_expected:
            raise Exception(f'Not enough arguments, {arguments_expected} expected')
        else:
            return spell_args
    else:
        return None


def substitute_args(text, args):
    i = 1
    for arg in args:
        text = text.replace('$' + str(i), arg)
        i = i+1
    return text


def display_message(spell, spell_args):
    message = spell.get("message")
    if spell_args is not None:
        message = substitute_args(message, spell_args)
    print(f'✨  {in_color(message, Colors.CYAN)}')


def parse_command(command, spell_args):
    if spell_args is not None:
        command = substitute_args(command, spell_args)
    return command


def cast_spell(arguments):
    try:
        spellbook = open_spellbook()
        magic_word = arguments['<spell>']
        spell_args = arguments['<args>']
        spell = spellbook.get(magic_word)

        if spell:
            spell_args = check_args(spell.get("argumentsExpected"), spell_args)
            display_message(spell, spell_args)
            for command in spell['commands']:
                parsed_command = parse_command(command, spell_args)
                exit_code = WEXITSTATUS(system(parsed_command))
                if exit_code != 0:
                    raise Exception(f'Command returned exit code {exit_code}')
        else:
            raise Exception(f'Spell not found for magic word: {magic_word}')

    except Exception as error:
        print(f"""{Colors.RED}🔥 {error}{Colors.RESET}""")
        raise RuntimeError
