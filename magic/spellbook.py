import json
import os
from shutil import copyfile

from fastjsonschema import validate
from .config import SPELLBOOK_PATH, SPELLBOOK_SCHEMA_PATH, DEFAULT_SPELLBOOK_PATH
from .utils import Colors, in_color


def check_spellbook(spellbook_contents):
    try:
        with open(SPELLBOOK_SCHEMA_PATH, 'r') as spellbook_schema:
            schema = json.load(spellbook_schema)
        validate(schema, spellbook_contents)
    except Exception as error:
        raise Exception(f'Spellbook is invalid: {error}')


def read_spellbook(spellbook_contents):
    spells = dict()
    for entry in spellbook_contents:
        for magic_word in entry['magicWords']:
            if spells.get(magic_word):
                raise Exception(f'Spellbook has duplicated magic word: {magic_word}')
            spells[magic_word] = entry
    return spells


def get_spells():
    if not os.path.exists(SPELLBOOK_PATH):
        copyfile(DEFAULT_SPELLBOOK_PATH, SPELLBOOK_PATH)

    with open(SPELLBOOK_PATH, 'r') as spellbook_file:
        spellbook_contents = json.load(spellbook_file)
    check_spellbook(spellbook_contents)
    return read_spellbook(spellbook_contents)


def list_spells():
    spells = get_spells()
    for magic_word, spell in sorted(spells.items()):
        print(f'{in_color(magic_word, Colors.CYAN)}: {spell.get("description")}')


def show_spell(spell, spell_args):
    spells = get_spells()
    spell = spells.get(spell)
    color = Colors.MAGENTA

    print(f'{in_color("Description:", color)} {spell["description"]}')
    print(f'{in_color("Magic words:", color)} {", ".join(spell["magicWords"])}')
    print(in_color("Commands:", color))
    for command in spell['commands']:
        print(f'{command}')

    argument_count = spell.get("argumentCount")
    if argument_count is None:
        print(f'{in_color("Arguments required:", color)} None')
    else:
        arg_color = Colors.GREEN if len(spell_args) == argument_count else Colors.RED
        print(f'{in_color("Arguments required:", color)} {in_color(argument_count, arg_color)}')

    print(in_color("Arguments provided:", color))
    for idx, arg in enumerate(spell_args):
        print(f'  {idx}: {arg}')
