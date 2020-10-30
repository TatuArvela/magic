"""✨ Magic ✨

Usage:
    magic <spell>
    magic show <spell>
    magic -h | --help
    magic -v | --version

Options:
    -h --help       show this
    -v --version    show version"""

import sys
import os
import configparser
from docopt import docopt
import app

if __name__ == '__main__':
    # Change working directory to script directory
    abspath = os.path.abspath(sys.argv[0])
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # Load configuration
    config = configparser.ConfigParser()
    config.read(os.path.join(dname, 'magic/config.ini'))

    version = config.get("app", "version")
    arguments = docopt(__doc__, version=f'v{version}, © 2020 Tatu Arvela')

    # Case if the user omits arguments
    if (arguments["<spell>"] == None):
        print(__doc__)
        sys.exit()

    # pylint: disable=E1121
    app.run(arguments, config)
