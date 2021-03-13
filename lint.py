import subprocess

from magic.utils.display import Colors, in_color


def lint():
    print(in_color("# Running isort", Colors.BLUE))
    subprocess.run(["isort", "."])
    print(in_color("# Running black", Colors.BLUE))
    subprocess.run(["black", "."])
    print(in_color("# Running flake8", Colors.BLUE))
    subprocess.run(["flake8", "."])
    print(in_color("# Running bandit", Colors.BLUE))
    subprocess.run(["bandit", "-r", "--ini", ".bandit"])


if __name__ == "__main__":
    lint()
