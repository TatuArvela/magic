import json
from fastjsonschema import validate, JsonSchemaException
from magic import SPELLBOOK_PATH, Colors


def validate_spellbook(spellbook_contents):
    with open('magic/spellbook-schema.json', 'r') as spellbook_schema:
        schema = json.load(spellbook_schema)

    try:
        validate(schema, spellbook_contents)
    except JsonSchemaException as err:
        raise Exception(f"""{Colors.RED}Spellbook validation error: {err}{Colors.RESET}""")


def open_spellbook():
    with open(SPELLBOOK_PATH, 'r') as spellbook_file:
        spells = json.load(spellbook_file)
    validate_spellbook(spells)
    return spells
