from magic.utils.display import Color, in_color
from magic.utils.spellbook import get_spells


def list_spells():
    spells = get_spells()
    if len(spells) == 0:
        print(f'{in_color("Your spellbook is empty", Color.CYAN)}')
    for magic_word, spell in sorted(spells.items()):
        print(f'{in_color(magic_word, Color.CYAN)}: {spell.get("description")}')
