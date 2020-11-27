"""✨  \u001b[34mMagic\u001b[0m

Usage:
    magic [--show] <spell> [<args>...]
    magic -s | --show
    magic -h | --help
    magic -v | --version

Options:
    -s --show       show spell(s)
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


def print_result(start_time, success):
    current_time = datetime.now().strftime('%H:%M:%S')
    elapsed_time = datetime.now() - start_time
    elapsed_time = elapsed_time - timedelta(microseconds=elapsed_time.microseconds)

    emoji = '✅ ' if success else '❌️'
    message = in_color('Success', Colors.GREEN) if success else in_color('Failure', Colors.RED)

    print(f'{emoji} {in_color(current_time, Colors.CYAN)} {message} ⏱  {elapsed_time}')


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
