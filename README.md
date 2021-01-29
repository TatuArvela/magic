# Magic

**✨ Magic** is a tool for managing command line scripts.

## Usage

**Magic** can be used to simplify often repeated tasks such as starting servers and deploying applications.

*TODO* ~~Scripts can also be registered from commands or **Makefiles**, which are linked into a JSON format file called the **Spellbook** (`Spellbook.json`). Working directory is registered as well.~~

Each spell is given a **message** and one or several **magic words** (identifiers) used to call it.

## Credits

I used [MartinHeinz/python-project-blueprint](https://github.com/MartinHeinz/python-project-blueprint) as a starting point to bring this project up to standards. Thank you, Martin!

## TODO

* Persist working directory between commands
* Supplying custom spellbook from environment variable
* Spell registration wizard
* Testing
* coverage.py
