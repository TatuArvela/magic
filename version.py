import re
import subprocess
import sys


def increment_version(param):
    command = f"poetry version {param}"
    output = subprocess.run(command.split(" "), capture_output=True)
    decoded_stdout = output.stdout.decode()
    print(decoded_stdout.strip())
    new_version = re.search(r"(\d+\.\d+\.\d+)$", decoded_stdout).group()
    return new_version


def commit_and_tag(version):
    commands = [
        "git add -u",
        f"git commit -m v{version}",
        f"git tag v{version}"
    ]
    for command in commands:
        subprocess.run(command.split(" "))


def push_to_origin(version):
    commands = [
        "git push origin master",
        f"git push origin v{version}",
    ]
    for command in commands:
        subprocess.run(command.split(" "))


def main(argv):
    if len(argv) == 0:
        print("Specify one of the following as an argument: patch, minor, major")
        exit(1)
    param = argv[0]

    new_version = increment_version(param)
    commit_and_tag(new_version)
    push_to_origin(new_version)


if __name__ == "__main__":
    main(sys.argv[1:])
