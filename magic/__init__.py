"""A tool for simplifying repeated command line tasks

Usage:
    magic [-s | --show] <spell> [<args>...]
    magic -a | --add
    magic -l | --list
    magic -h | --help
    magic -v | --version

Options:
    -s --show       show spell details
    -a --add        add spell to spellbook
    -l --list       list spells in spellbook
    -h --help       show this
    -v --version    show version"""

from datetime import datetime, timedelta
from docopt import docopt
from sys import exit

from magic.add import add_spell
from magic.cast import cast_spell
from magic.show import show_spell
from magic.list import list_spells
from magic._version import __version__
from magic.utils.display import Colors, in_color, print_error

VERSION_STRING = f'✨ {in_color("Magic", Colors.BLUE)} v{__version__}, © 2021 Tatu Arvela'
DOC_STRING = f'{VERSION_STRING}\n{__doc__}'


def main():
    arguments = docopt(DOC_STRING, version=VERSION_STRING)

    show_arg = arguments["--show"]
    add_arg = arguments["--add"]
    list_arg = arguments["--list"]
    spell = arguments["<spell>"]
    spell_args = arguments["<args>"]

    if show_arg is True:
        if spell:
            try:
                show_spell(spell=spell, spell_args=spell_args)
            except Exception as error:
                print_error(error)
        else:
            # Invalid usage
            print(__doc__)
        exit()

    if add_arg is True:
        try:
            add_spell()
        except Exception as error:
            print_error(error)
        exit()

    if list_arg is True:
        try:
            list_spells()
        except Exception as error:
            print_error(error)
        exit()

    handle_spell_cast(arguments)


def handle_spell_cast(arguments):
    start_time = datetime.now()

    try:
        show_success_message = cast_spell(arguments)
        if show_success_message:
            print_result(start_time, success=True)

    except RuntimeError:
        print_result(start_time, success=False)


def print_result(start_time, success):
    current_time = datetime.now().strftime('%H:%M:%S')
    elapsed_time = datetime.now() - start_time
    elapsed_time = elapsed_time - timedelta(microseconds=elapsed_time.microseconds)

    emoji = '✅' if success else '❌️'
    message = in_color('Success', Colors.GREEN) if success else in_color('Failure', Colors.RED)

    print(f'{emoji} {in_color(current_time, Colors.CYAN)} {message} ⏱ {elapsed_time}')
