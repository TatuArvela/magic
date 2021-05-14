from click import Context, Group

from magic.shared.display import Color, in_color
from magic.shared.spellbook import get_spells
from magic.version import version_text


def get_magic_words():
    spells = get_spells()

    if len(spells) == 0:
        return ""

    max_word_length = max(len(magic_word) for magic_word in spells)
    spacing = 2
    output = "Magic words:"
    for magic_word, spell in sorted(spells.items()):
        indent = max_word_length + spacing - len(magic_word)
        output = (
            output
            + f'\n  {in_color(magic_word, Color.CYAN)}{" " * indent}{spell.get("description")}'
        )
    return output


def get_help(self, ctx: Context):
    click_help = Group.get_help(self, ctx)
    without_usage = "\n".join(click_help.splitlines()[1:])
    description = "A tool for simplifying repeated command line tasks"

    return (
        f"{version_text}\n"
        f"{description}\n"
        f"\n"
        f"Usage:\n"
        f"  magic <OPTIONS> COMMAND [ARGS]...\n"
        f"  magic MAGIC_WORD [ARGS]...\n"
        f"{without_usage}"
    )
