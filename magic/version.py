from importlib import metadata

from magic.shared.display import EMOJI_SPARKLE, Color, in_color

name = "Magic"
version = metadata.version("tatuarvela-magic")
year = 2021
author = "Tatu Arvela"

version_text = (
    f"{EMOJI_SPARKLE} {in_color(name, Color.BLUE)} v{version} (c) {year} {author}"
)


def show_version():
    print(version_text)
