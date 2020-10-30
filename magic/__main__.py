"""✨ Magic ✨

Usage:
    magic <spell>
    magic show <spell>
    magic -h | --help
    magic -v | --version

Options:
    -h --help       show this
    -v --version    show version

"""
from docopt import docopt
from .app import Magic

VERSION = "3"

if __name__ == '__main__':
    arguments = docopt(__doc__, version=f'v{VERSION}, © 2020 Tatu Arvela')
    # pylint: disable=E1121
    Magic.run(arguments)
