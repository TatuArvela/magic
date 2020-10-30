"✨ Magic"

import json

spellbook = {}

def load_spellbook(config):
    spellbookPath = config.get('app', 'spellbookPath')
    with open(spellbookPath, 'r') as spellbook:
        return json.load(spellbook)

def run(arguments, config):
    global spellbook
    spellbook = load_spellbook(config)

    print(spellbook)

    print(arguments)