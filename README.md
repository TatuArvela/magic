# Magic

**✨ Magic** is a tool for simplifying repeated command line tasks.

## Concepts

* **Magic** simplifies a set of commands into a **spell**
* Spells are written into the **spellbook** (`Spellbook.json`)
* Each spell has one or several **magic words** that can be used to call it  
  e.g. `magic build-app` and `magic ba`
* Spells can have **arguments** passed to them  
  e.g. `magic say abra kadabra`
* The execution time of spells is measured by default
* **📝 TODO:** Spells can be entered into the spellbook using a **wizard**
* **📝 TODO:** Spells can be edited
* **📝 TODO:** Spells can be removed

## Usage

### Installation

Installation is currently manual. Follow the instructions below.

Requirements: Python 3

1. Clone the project somewhere and navigate to it on the command line
2. Create a virtual env  
        `python3 -m venv env`

3. Activate the virtual environment  
        `source env/bin/activate`

4. Install the requirements  
        `pip install -r requirements.txt`

5. Verify that the application works  
        `python3 -m magic`
6. Add `Magic/bin` to your PATH to use `magic`

### Parameters

```
$ magic --help
✨  Magic

Usage:
    magic [-s | --show] <spell> [<args>...]
    magic -a | --add
    magic -l | --list
    magic -h | --help
    magic -v | --version

Options:
    -s --show       show spell details
    -a --add        add spell to spellbook
    -l --list       list spells in spellbook
    -h --help       show this
    -v --version    show version
```

### Spell wizard

### Spell arguments

Spells can have an array of arguments, which are populated according to their index. Excessive usage is considered an anti-pattern.

Example:

```
{
  "description": "Test echo spell with arguments '$0' and '$1'",
  "magicWords": [
    "t",
    "test"
  ],
  "commands": [
    "echo $0",
    "echo $1"
  ],
  "argumentsExpected": 2
},
```

```
$ magic test cat dog
✨  Test echo spell with arguments 'cat' and 'dog'
cat
dog
✅ 17:00:00 Success ⏱ 0:00:00
```

#### Advanced usage: Empty arguments

Argument are handled as an array, so arguments can not be empty. As a work-around they may be substituted with an empty string: `''`.

#### Advanced usage: Spell options

It is possible to provide options (`--option`) as arguments to spells. This is not intended usage, but may be useful to some.

This requires a little work-around, as `docopt` stops the execution if it detects unknown options. You can provide the options your spell requires by adding a space and quotes `' --option'`.

## Development

**📝 TODO:** Installation script

**📝 TODO:** coverage.py

**📝 TODO:** Testing

## Credits

* I used [MartinHeinz/python-project-blueprint](https://github.com/MartinHeinz/python-project-blueprint) as a basic guide for creating a proper Python project. Thank you, Martin!
* Developed with the support of my employer, [Nitor](https://nitor.com/)
