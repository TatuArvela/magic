"""✨ Magic"""
from magic.spellbook import open_spellbook

spellbook = None


def run(arguments):
    global spellbook
    spellbook = open_spellbook()

    print(arguments)
