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

**📝 TODO:** Fill documentation

### Installation

### Parameters

### Working directory

**📝 TODO:** Persist working directory changes between commands

### Spell wizard

### Spell arguments

Spells can have an array of arguments. Each argument must not be empty.

```
{
  "description": "Test echo spell with arguments '$1' and '$2'",
  "magicWords": [
    "t",
    "test"
  ],
  "commands": [
    "echo $1",
    "echo $2"
  ],
  "argumentsExpected": 2
},
```

**📝 TODO:** Enabling `n` arguments

**📝 TODO:** Ensuring no clashes with `docopt`

## Development

**📝 TODO:** Testing

**📝 TODO:** coverage.py

## Credits

* I used [MartinHeinz/python-project-blueprint](https://github.com/MartinHeinz/python-project-blueprint) as a basic guide for creating a proper Python project. Thank you, Martin!
* Developed with the support of my employer, [Nitor](https://nitor.com/)
