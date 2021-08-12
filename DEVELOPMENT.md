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

2. Install `magic` and its dependencies to a virtual env

   ```bash
   poetry install
   ```

3. Verify that `magic` works

   ```bash
   poetry run magic
   ```

4. Register `magic` to your `PATH`

    ```bash
    python -m write_path
    ```

When developing the tool, you should use the `magic` module directly
with `python -m magic`.

After successful changes, you need to run `poetry install` again to update the
version in your `PATH`.

## 💎 Code quality tools

Magic uses `isort`, `black` and `flake8` as its code quality tools. They are
executed automatically with `pre-commit` and can also be executed with the
included lint script:

```bash
python -m lint
```

## 📜 TODO

### 👷 Next release
* Add `pytest`, `snapshottest`, `coverage.py`
* Improve Python version support
  
### 🧑‍🚀 Future releases
* Add `update(spell)`
  * Create prompt with user-editable prefilled data
* Improved `add_spell` wizard
  * Enable browsing command line history in order to create spells faster
