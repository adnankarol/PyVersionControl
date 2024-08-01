__author__ = "Adnan Karol"
__version__ = "1.0.0"
__maintainer__ = "Adnan Karol"
__email__ = "adnanmushtaq5@gmail.com"
__status__ = "DEV"

# Import Dependencies
import os
import argparse
import glob
import time
import shutil
from distutils.dir_util import copy_tree


def parse_args():
    parser = argparse.ArgumentParser(description='Version Control: BIT.')
    parser.add_argument('--path', required=True, help='Please enter the path to the folder')
    parser.add_argument('--command', required=True, help='Please enter the command if needed')
    return parser.parse_args()


def get_size(filename):
    return os.path.getsize(filename)


def create_bit_folder(path):
    bit_version_path = os.path.join(path, "bit_version")
    if not os.path.exists(bit_version_path):
        os.makedirs(bit_version_path)


def create_base_version(path):
    version_path = os.path.join(path, "bit_version", "version_1")

    if not os.path.exists(version_path):
        os.makedirs(version_path)

        with open(os.path.join(version_path, "commit_message.txt"), "a") as f:
            f.write(f"version_{time.time()} : Commit Message : Initial Code")

        temp_path = os.path.join(path, "temp")
        if not os.path.exists(temp_path):
            os.makedirs(temp_path)

        copy_tree(path, temp_path)
        shutil.rmtree(os.path.join(temp_path, "bit_version"), ignore_errors=True)
        shutil.rmtree(temp_path, ignore_errors=True)
        copy_tree(temp_path, version_path)
        shutil.rmtree(temp_path)

        return True
    return False


def read_versions(path):
    print("*" * 80)
    for filename in glob.glob(os.path.join(path, "bit_version", "*")):
        with open(os.path.join(filename, "commit_message.txt"), "r") as myfile:
            data = myfile.readline().strip()
            print(data)
    print("*" * 80)


def commit_changes(path, commit_message):
    change_detected = False
    current_time = str(time.time())
    latest_version_folder = os.path.join(path, "bit_version", "*")
    latest_version_file = os.path.join(path, "bit_version", "version_1")

    try:
        for filename in glob.glob(latest_version_folder):
            if latest_version_file != "version_1":
                if int(filename.split("_")[-1].split(".")[0]) > int(latest_version_file.split("_")[-1].split(".")[0]):
                    latest_version_file = filename
    except Exception:
        pass

    for filename in glob.glob(os.path.join(path, "*")):
        if "bit_version" not in filename:
            filesize_base = get_size(filename)
            try:
                filesize_last_commit = get_size(os.path.join(latest_version_file, os.path.basename(filename)))
            except FileNotFoundError:
                print("File Added:", filename)
                filesize_last_commit = 0

            if filesize_base != filesize_last_commit:
                print("File Changed:", os.path.basename(filename))
                change_detected = True

    if change_detected:
        new_version_path = os.path.join(path, "bit_version", f"version_{current_time}")
        os.makedirs(new_version_path)
        for filename in glob.glob(os.path.join(path, "*")):
            if "bit_version" not in filename:
                shutil.copy(filename, new_version_path)

        with open(os.path.join(new_version_path, "commit_message.txt"), "a") as f:
            f.write(f"version_{current_time} : Commit Message : {commit_message}")
    else:
        print("Warning: No file changed!")


def main():
    args = parse_args()
    path_to_folder = args.path
    command = args.command

    print("The project path entered is:", path_to_folder)

    create_bit_folder(path_to_folder)
    if create_base_version(path_to_folder):
        print("Initial Commit")
        return

    if command == "list_versions":
        read_versions(path_to_folder)
    elif "commit" in command:
        commit_message = command.split("-", 1)[-1] if '-' in command else "No commit message provided"
        commit_changes(path_to_folder, commit_message)


if __name__ == "__main__":
    main()
