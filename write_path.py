# Adds the development version of Magic to your PATH

import os

SHELL = os.getenv("SHELL", "")
BIN_DIR = os.path.join(os.path.dirname(__file__), "bin")
HOME = os.path.expanduser("~")


def __get_unix_profiles():
    profiles = [os.path.join(HOME, ".profile")]

    if "zsh" in SHELL:
        zdotdir = os.getenv("ZDOTDIR", HOME)
        profiles.append(os.path.join(zdotdir, ".zshrc"))

    bash_profile = os.path.join(HOME, ".bash_profile")
    if os.path.exists(bash_profile):
        profiles.append(bash_profile)

    return profiles


def __get_export_string():
    export_string = f'export PATH="$PATH:{BIN_DIR}"'

    return export_string


def write_path():
    print("Adding magic to your PATH...")
    export_string = __get_export_string()
    magic_section = f"\n{export_string}\n"

    profiles = __get_unix_profiles()
    for profile in profiles:
        if not os.path.exists(profile):
            print(f"Skipped profile: {profile}")
            continue

        with open(profile, "r") as f:
            content = f.read()

        if magic_section not in content:
            with open(profile, "a") as f:
                f.write(str(magic_section))
            print(f"Added to profile: {profile}")
        else:
            print(f"Already included in: {profile}")


if __name__ == "__main__":
    write_path()
