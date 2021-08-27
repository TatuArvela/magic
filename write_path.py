# Adds the development version of Magic to your PATH

import os
import sys

SHELL = os.getenv("SHELL", "")
BIN_DIR = os.path.join(os.path.dirname(__file__), "bin")
HOME = os.path.expanduser("~")


def __get_config_file():
    if "bash" in SHELL:
        bash_config = os.path.join(HOME, ".bashrc")
        return bash_config

    if "zsh" in SHELL:
        zdotdir = os.getenv("ZDOTDIR", HOME)
        zsh_config = os.path.join(zdotdir, ".zshrc")
        return zsh_config

    print(f"Your shell ({SHELL}) is not yet supported by this tool.")
    sys.exit(1)


def __get_export_string():
    export_string = f'export PATH="$PATH:{BIN_DIR}"'

    return export_string


def write_path():
    print("Adding Magic to your PATH...")
    export_string = __get_export_string()
    magic_section = f"\n{export_string}\n"

    config_file = __get_config_file()

    if not os.path.exists(config_file):
        print(f"Config file ({config_file}) does not exist")
        sys.exit(1)

    with open(config_file, "r+", encoding="utf-8") as file:
        # Important for .write(), as this moves the position to the end
        content = file.read()

        if magic_section not in content:
            file.write(str(magic_section))
            print(f"Added Magic to config file ({config_file})")
        else:
            print(f"Magic is already included in config file ({config_file})")


if __name__ == "__main__":
    write_path()
