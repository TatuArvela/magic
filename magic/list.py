from magic.utils.spellbook import get_spells
from magic.utils.display import in_color, Colors


def list_spells():
    spells = get_spells()
    for magic_word, spell in sorted(spells.items()):
        print(f'{in_color(magic_word, Colors.CYAN)}: {spell.get("description")}')
