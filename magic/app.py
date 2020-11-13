"""✨ Magic"""
from magic.utils import Colors
from magic.spellbook import open_spellbook

spellbook = None


def run(arguments):
    global spellbook

    try:
        spellbook = open_spellbook()
        magic_word = arguments['<spell>']
        spell = spellbook.get(magic_word)

        if spell:
            print(spell)
        else:
            raise Exception(f'Spell not found for magic word: {magic_word}')

    except Exception as error:
        print(f"""{Colors.RED}🔥 {error}{Colors.RESET}""")
