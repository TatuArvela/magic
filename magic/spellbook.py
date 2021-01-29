import json
from fastjsonschema import validate
from .config import SPELLBOOK_PATH
from .utils import Colors, in_color


def validate_spellbook(spellbook_contents):
    try:
        with open('magic/spellbook.schema.json', 'r') as spellbook_schema:
            schema = json.load(spellbook_schema)
        validate(schema, spellbook_contents)
    except Exception as error:
        raise Exception(f'Spellbook is invalid: {error}')


def parse_spellbook(spellbook_contents):
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
    return parse_spellbook(spellbook_contents)


def list_spells():
    spellbook = open_spellbook()
    for magic_word, spell in sorted(spellbook.items()):
        print(f'{in_color(magic_word, Colors.CYAN)}: {spell.get("description")}')


def show_spell(spell, spell_args):
    spellbook = open_spellbook()
    spell = spellbook.get(spell)
    color = Colors.MAGENTA

    print(f'{in_color("Message:", color)} {spell["message"]}')
    print(f'{in_color("Magic words:", color)} {spell["magicWords"]}')
    print(in_color("Commands:", color))
    for command in spell['commands']:
        print(f'  {command}')

    arguments_expected = spell.get("argumentsExpected")
    if arguments_expected is not None:
        arg_color = Colors.GREEN if len(spell_args) == arguments_expected else Colors.RED
        print(f'{in_color("Arguments expected:", color)} {in_color(arguments_expected, arg_color)}')

    print(in_color("Arguments provided:", color))
    for idx, arg in enumerate(spell_args):
        print(f'  {idx + 1}: {arg}')
