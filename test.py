import subprocess


def header(text):
    print(f"# \u001b[34m{text}\u001b[0m")


def run(command, check=False):
    subprocess.run(command.split(" "), check=check)


def test():
    header("Running unittest with coverage")
    run("coverage run -m pytest")

    header("Running coverage report")
    run("coverage report")


if __name__ == "__main__":
    test()
