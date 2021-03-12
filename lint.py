import subprocess

BLUE = "\033[0;34m"
NO_COLOR = "\033[0m"


def lint():
    print(f"{BLUE}# Running isort{NO_COLOR}")
    subprocess.run(["isort", "."])
    print(f"{BLUE}# Running black{NO_COLOR}")
    subprocess.run(["black", "."])
    print(f"{BLUE}# Running flake8{NO_COLOR}")
    subprocess.run(["flake8", "."])


if __name__ == "__main__":
    lint()
