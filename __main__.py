"""\u2728  \u001b[34mMagic\u001b[0m \u2728\t

Usage:
    magic <spell>
    magic show <spell>
    magic -h | --help
    magic -v | --version

Options:
    -h --help       show this
    -v --version    show version"""

import sys
from docopt import docopt
from magic import app, VERSION

if __name__ == '__main__':
    arguments = docopt(__doc__, version=f'v{VERSION}, © 2020 Tatu Arvela')

    # Case if the user omits arguments
    if arguments["<spell>"] is None:
        print(__doc__)
        sys.exit()

    app.run(arguments)
