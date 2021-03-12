![Magic](./Magic.png "Magic")

**✨ Magic** is a tool for wrapping repeated command line tasks into simple scripts.

* A set of commands is saved as a **spell**
* Spells are written into the **spellbook** file (`~/.spellbook.json`)
* Each spell can be called with one or several **magic words**  
  e.g. `magic build-app` and `magic ba`
* Spells can have **arguments** passed to them  
  e.g. `magic say abra kadabra`
* The execution time of spells is reported by default

## Installation

Installation is currently manual. Follow the instructions below.

* Supported operating systems: macOS (untested on Linux and Windows)
* Requirements: Python 3, Poetry

1. Clone the Git repository somewhere and navigate to it on the command line
   ```
   git clone https://github.com/TatuArvela/Magic.git
   cd Magic
   ```

2. Create a virtual env and install requirements
   ```
   poetry install
   ```

3. Verify that the application works
   ```
   python3 -m magic
   ```

4. Add `Magic/bin` to your PATH in your `.bashrc`, `.zshrc` or other configuration file
    ```
    # Magic
    export PATH="$PATH:<CLONING_DIRECTORY_HERE>/Magic/bin"
    ```

## Usage

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

Editing a spell is currently done with an external editor (**Visual Studio Code** by default).

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

### TODO before v3.0.0 release

#### Release tools

* Package metadata and structure
      * build
      * publish
      * test
      * clean
* Pipeline that pops out a release artifact (a binary that requires just Python 3)
* CI pipeline that triggers this on a new tagged release

#### Testing

* coverage.py
* pytest

## Credits

* Developed with the support of my employer, [Nitor](https://nitor.com/)
