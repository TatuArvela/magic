from click import Context, Group

from magic.version import version_text


def get_help(self, ctx: Context):
    click_help = Group.get_help(self, ctx)
    description = "A tool for simplifying repeated command line tasks"

    return f"{version_text}\n" f"{description}\n" f"\n" f"{click_help}"
