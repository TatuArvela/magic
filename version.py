import re
import subprocess
import sys


def increment_str_int(str_int):
    return str(int(str_int) + 1)


# Get a value in a nested dict by a string key
def get_by_key(dic, key):
    split_key = key.split('.')
    return_value = dic
    for key in split_key:
        return_value = return_value.get(key, {})
    return return_value


# Set a value in a nested dict by a string key
def set_by_key(dic, key, value):
    split_key = key.split('.')
    for key in split_key[:-1]:
        dic = dic.setdefault(key, {})
    dic[split_key[-1]] = value


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
