# Magic

Magic is a shortcut and abstraction tool for command line scripts. It can be used to simplify often repeated tasks such as starting servers and deploying applications. It is designed to be customizable to fit various needs.

Scripts and tasks are called **spells**, which can be defined in a YAML file called the **spellbook** (`spellbook.yml`). Each spell has a **message**, one or several **magic words** (identifiers) and one or several **conjurations** (console commands). Several spells can be cast in succession by separating them with a comma (`,`), for example `magic start-dev-server, deploy-frontend dev`. Spells can also have short forms, for example `magic sd, df dev`.

Variables can be passed on the command line (`magic spell variable1 variable2 ...`) or they can be predefined in the `environment_variables` section of the `config.yml` file. The amount of passed variables required by a spell can be defined in the spellbook with the optional field `variables_required`.

## Installation instructions for Ubuntu 17.10+

1. Install Python 3
2. Copy the application to `/home/<username>/bin/` (If this folder does not yet exist, create it and log out and back in)
3. Make a copy of `spellbook.yml` to `/home/<username>/.config/magic/spellbook.yml`
4. Make a copy of `config.yml` to `/home/<username>/.config/magic/config.yml`
5. Check that the application works by running `magic`
6. Add your own configurations to your spellbook