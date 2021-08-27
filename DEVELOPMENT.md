# ⚙️ Development

## 🐍 Installation

* Supported operating systems: macOS (untested on Linux)
* Requirements: Python ^3.7, Poetry

Magic uses [Poetry](https://python-poetry.org/) as a packaging and dependency management tool. It uses the rather
new `pyproject.toml` format, proposed in [PEP-517](https://www.python.org/dev/peps/pep-0517/).

1. Clone the Git repository somewhere and navigate to it on the command line

    ```bash
    git clone https://github.com/TatuArvela/Magic.git
    cd Magic
    ```

2. Create a virtualenv and install `magic` and its dependencies

    ```bash
    poetry install

    # You can also install just the dependencies required by the project
    poetry install --no-root
    ```

3. Verify that the installed version of `magic` works (if you installed it)

    ```bash
    poetry run magic
   
    # While developing (or if you used the '--no-root' option) you can run the module directly
    poetry run python -m magic
    ```

4. (Optional) Register the virtualenv version of `magic` to your `PATH`

    ```bash
    poetry run python -m write_path
   
    # The script adds the path to .bashrc or .zshrc, depending on the current shell
    ```

## 🔧 Usage

When developing the tool, run the module directly:

```bash
poetry run python -m magic

# You can also enter the virtualenv to run commands without the 'poetry run' prefix
poetry shell
python -m magic
```

After successful changes, you can update the installed version and test it:

```bash
poetry install
```

```bash
poetry run magic

# If you are in the virtualenv, or registered the installed version to your path
magic
```

## 🧪 Testing

Magic uses `pytest`, `snapshottest` and `coverage.py` for testing. They are executed automatically with `pre-commit`
and can also be executed with the included test script:

```bash
# Assuming virtualenv is active
python -m test
```

## 💎 Code formatting and analysis

Magic uses `isort`, `black`, `pylint` and `bandit` to check for problems. They are executed automatically with `pre-commit`
and can also be executed with the included lint script:

```bash
# Assuming virtualenv is active
python -m lint
```

## 📝 TODO

### 🔮 Future releases

* Add `update(spell)`
    * Create prompt with user-editable prefilled data
* Improve `add_spell` wizard
    * Enable context awareness and/or browsing command line history in order to create useful spells faster
