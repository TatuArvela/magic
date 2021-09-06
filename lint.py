import subprocess


def header(text):
    print(f"# \u001b[34m{text}\u001b[0m")


def run(command, check=False):
    subprocess.run(command.split(" "), check=check)


def lint():
    header("Running isort")
    run("isort .")

    header("Running black")
    run("black .")

    header("Running pylint")
    run("pylint magic write_path.py")

    header("Running bandit")
    run("bandit -r --ini .bandit")


if __name__ == "__main__":
    lint()
