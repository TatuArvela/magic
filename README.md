# Magic

**✨ Magic** is a tool for simplifying repeated command line tasks.

## Concepts

* **Magic** simplifies a set of commands into a **spell**
* Spells are written into the **spellbook** (`spellbook.json`)
* Each spell has one or several **magic words** that can be used to call it  
  e.g. `magic build-app` and `magic ba`
* Spells can have **arguments** passed to them  
  e.g. `magic say abra kadabra`
* The execution time of spells is measured by default

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
✨ Magic v3.0.0, © 2021 Tatu Arvela
A tool for simplifying repeated command line tasks

Usage:
    magic [-s | --show] <spell> [<args>...]
    magic [-d | --delete] <spell>
    magic -a | --add
    magic -e | --edit
    magic -l | --list
    magic -h | --help
    magic -v | --version

Options:
    -s --show       show spell details
    -d --delete     delete spell from spellbook
    -a --add        add spell to spellbook
    -e --edit       edit spellbook
    -l --list       list spells in spellbook
    -h --help       show help
    -v --version    show version
```

### Spell wizard

### Spell arguments

Spells can have an array of arguments, which are populated according to their index. Excessive usage is considered an
anti-pattern.

Example:

```
{
  "description": "Test echo spell with arguments '$a0' and '$a1'",
  "magicWords": [
    "t",
    "test"
  ],
  "commands": [
    "echo $a0",
    "echo $a1"
  ],
  "argumentCount": 2
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

Argument are handled as an array, so arguments can not be empty. As a work-around they may be substituted with an empty
string: `''`.

#### Advanced usage: Spell options

It is possible to provide options (`--option`) as arguments to spells. This is not intended usage, but may be useful to
some. This requires a little work-around, as `docopt` stops the execution if it detects unknown options. You can provide
the options your spell requires by adding a space and quotes `' --option'`.

## Development

**📝 TODO:** Installation script

**📝 TODO:** coverage.py

**📝 TODO:** Testing

## Credits

* I used [MartinHeinz/python-project-blueprint](https://github.com/MartinHeinz/python-project-blueprint) as a basic
  guide for creating a proper Python project. Thank you, Martin!
* Developed with the support of my employer, [Nitor](https://nitor.com/)
