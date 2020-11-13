import json
from fastjsonschema import validate
from magic import SPELLBOOK_PATH


def validate_spellbook(spellbook_contents):
    try:
        with open('magic/spellbook-schema.json', 'r') as spellbook_schema:
            schema = json.load(spellbook_schema)
        validate(schema, spellbook_contents)
    except Exception as error:
        raise Exception(f'Spellbook is invalid: {error}')


def list_spells(spellbook_contents):
    spells = dict()
    for entry in spellbook_contents:
        for magic_word in entry['magicWords']:
            if spells.get(magic_word):
                raise Exception(f'Spellbook has duplicated magic word: {magic_word}')
            spells[magic_word] = entry
    return spells


def open_spellbook():
    with open(SPELLBOOK_PATH, 'r') as spellbook_file:
        spellbook_contents = json.load(spellbook_file)
    validate_spellbook(spellbook_contents)
    return list_spells(spellbook_contents)

