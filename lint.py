import subprocess


def colorize(text):
    return f"\u001b[34m{text}\u001b[0m"


def lint():
    print(colorize("# Running isort"))
    subprocess.run(["isort", "."])
    print(colorize("# Running black"))
    subprocess.run(["black", "."])
    print(colorize("# Running flake8"))
    subprocess.run(["flake8", "."])
    print(colorize("# Running bandit"))
    subprocess.run(["bandit", "-r", "--ini", ".bandit"])


if __name__ == "__main__":
    lint()
