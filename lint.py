import subprocess


def colorize(text):
    return f"\u001b[34m{text}\u001b[0m"


def lint():
    print(colorize("# Running isort"))
    subprocess.run(["isort", "."], check=False)
    print(colorize("# Running black"))
    subprocess.run(["black", "."], check=False)
    print(colorize("# Running pylint"))
    subprocess.run(
        ["pylint", "magic", "tests", "lint.py", "test.py", "write_path.py"], check=False
    )
    print(colorize("# Running bandit"))
    subprocess.run(["bandit", "-r", "--ini", ".bandit"], check=False)


if __name__ == "__main__":
    lint()
