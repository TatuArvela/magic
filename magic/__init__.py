"""✨  \u001b[34mMagic\u001b[0m

Usage:
    magic [-s | --show] <spell> [<args>...]
    magic -l | --list
    magic -h | --help
    magic -v | --version

Options:
    -s --show       show spell
    -l --list       list spells
    -h --help       show this
    -v --version    show version"""

import sys
from datetime import datetime, timedelta
from docopt import docopt
from .cast import cast
from .spellbook import show_spell, list_spells
from .version import __version__
from .utils import Colors, in_color

VERSION = __version__


def main():
    start_time = datetime.now()
    arguments = docopt(__doc__, version=f'v{__version__}, © 2020 Tatu Arvela')

    show_arg = arguments["--show"]
    spell = arguments["<spell>"]
    spell_args = arguments["<args>"]

    # Catch invalid usage
    if spell == 'show' or spell == 'list':
        print(__doc__)
        sys.exit()

    if show_arg is True:
        if spell:
            show_spell(spell=spell, spell_args=spell_args)
        else:
            list_spells()
        sys.exit()

    try:
        cast(arguments)
        print_result(start_time, success=True)
    except RuntimeError:
        print_result(start_time, success=False)


def print_result(start_time, success):
    current_time = datetime.now().strftime('%H:%M:%S')
    elapsed_time = datetime.now() - start_time
    elapsed_time = elapsed_time - timedelta(microseconds=elapsed_time.microseconds)

    emoji = '✅ ' if success else '❌️'
    message = in_color('Success', Colors.GREEN) if success else in_color('Failure', Colors.RED)

    print(f'{emoji} {in_color(current_time, Colors.CYAN)} {message} ⏱  {elapsed_time}')
