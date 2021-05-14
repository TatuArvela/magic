import click

from magic.add import add_spell
from magic.cast import cast_spell
from magic.delete import delete_spell
from magic.edit import edit_spellbook
from magic.help import get_help
from magic.shared.display import Color, in_color
from magic.shared.spellbook import get_spells
from magic.show import show_spell
from magic.version import show_version

CONTEXT_SETTINGS = dict(allow_extra_args=True)


class MagicGroup(click.Group):
    def get_help(self, ctx):
        return get_help(self, ctx)


@click.group(cls=MagicGroup, context_settings=CONTEXT_SETTINGS)
def main():
    pass  # no-op


@main.command(name="add")
def __add():
    """Add spell to spellbook"""
    add_spell()


@main.command(name="delete")
@click.argument("magic_word", metavar="<magic_word>")
def __delete(magic_word):
    """Delete spell MAGIC_WORD from spellbook"""
    delete_spell(magic_word=magic_word)


@main.command(name="edit")
def __edit():
    """Edit spellbook"""
    edit_spellbook()


@main.command(
    name="show",
    context_settings=dict(allow_extra_args=True, ignore_unknown_options=True),
)
@click.argument("magic_word")
@click.pass_context
def __show(ctx, magic_word):
    """Show details for spell MAGIC_WORD"""
    show_spell(magic_word=magic_word, spell_args=ctx.args)


@main.command(name="version")
def __version():
    """Show version"""
    show_version()


def create_func(magic_word):
    @click.pass_context
    def f(ctx):
        cast_spell(magic_word=magic_word, arguments=ctx.args)
        return True

    return f


spells = get_spells()

for magic_word, spell in spells.items():
    main.command(
        name=magic_word,
        help=in_color(spell.get("description"), Color.CYAN),
        context_settings=dict(allow_extra_args=True, ignore_unknown_options=True),
    )(create_func(magic_word))
