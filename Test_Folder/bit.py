# Import Dependencies
import sys, os
import argparse
import glob
import time
import shutil
from distutils.dir_util import copy_tree


def argsparser():

    global path_to_folder
    global command
    parser = argparse.ArgumentParser(description='Version Control : BIT.')
    parser.add_argument('--path',  help='Please Enter the path to Folder')
    parser.add_argument('--command',  help='Please Enter the command if needed')

    args = parser.parse_args()
    path_to_folder = args.path
    command = args.command


def get_size(filename):
    filesize = os.path.getsize(filename)
    return filesize


def create_bit_folder(path_to_folder):
    # Function to check if Bit Base Folder exists if not create one 
    if not os.path.exists(path_to_folder + "/_bit_version"):
        os.makedirs(path_to_folder + "/_bit_version")


def create_base_version(path_to_folder):
    # Function to check if earlier version exists if not create one 
    version_path = path_to_folder + "/_bit_version/version_1"

    if not os.path.exists(version_path):
        os.makedirs(version_path)

        f = open(version_path + "/commit_message.txt", "a")
        f.write("version_" + str(time.time()) + " : Commit Message : Initial Code")
        f.close()
        
        # make temp dir
        if not os.path.exists(path_to_folder + "/temp"):
            os.makedirs(path_to_folder + "/temp")
        
        copy_tree(path_to_folder, path_to_folder + "/temp")
        shutil.rmtree(path_to_folder + "/temp" + "/bit_version")
        shutil.rmtree(path_to_folder + "/temp" + "/temp")
        # Copy contents of folder
        copy_tree(path_to_folder + "/temp", version_path)
        shutil.rmtree(path_to_folder + "/temp")
        return 1


def read_versions(path_to_folder):
    print("*" * 80)
    for filename in glob.glob(path_to_folder + "/bit_version/*"):
        with open (filename + "/commit_message.txt", "r") as myfile:
            data=myfile.readlines()
            print(data[0])
    print("*" * 80)


def commit_changes(path_to_folder):
    change = 0
    current_time = str(time.time())
    commit_message = command.split("-")[-1]

    latest_version_folder = path_to_folder + "/_bit_version/*"
    latest_version_file = path_to_folder + "/_bit_version/version_1"

    try :
        for filename in glob.glob(latest_version_folder):
            if latest_version_file != "version_1":
                latest_version_file =  filename
                if int(filename.split("_")[-1].split(".")[0]) > int(latest_version_file.split("\\")[-1].split("_")[-1].split(".")[0]):
                    latest_version_file = filename
    except :
        pass

    for filename in glob.glob(path_to_folder + "/*"):

        if "_bit_version" not in filename:
            filesize_base = get_size(filename)
            filesize_last_commit = get_size(latest_version_file + "/" + filename.split("\\")[-1])

            if filesize_base != filesize_last_commit:
                change = 1
                print("File Changed : ", filename.split("\\")[-1] )

            if filesize_base == 0 :
                change = 1
                print("File Removed : " , filename)

        if change == 1:
            if not os.path.exists(path_to_folder + "/_bit_version/version_" + current_time):
                os.makedirs(path_to_folder + "/_bit_version/version_" + current_time)
            shutil.copy(filename,path_to_folder + "/_bit_version/version_" + current_time)

    if change !=0:
        f = open(path_to_folder + "/_bit_version/version_" + current_time + "/commit_message.txt", "a")
        f.write("version_" + current_time + " : Commit Message : " + commit_message )
        f.close()
    else :
        print("Warning : No File Changed!!")


def main():
    print("The Project Path Entered is : ", path_to_folder)

    create_bit_folder(path_to_folder)
    base_version = create_base_version(path_to_folder)

    if base_version == 1:
        print("Initial Commit")
        sys.exit(1)

    if command == "list_versions" :
        read_versions(path_to_folder)

    if "commit" in command :
        commit_changes(path_to_folder)


if __name__ == "__main__": 
    argsparser()
    main()