from magic.utils.spellbook import get_spells
from magic.utils.display import Colors, in_color


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
