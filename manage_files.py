#!/usr/bin/env python3

# JVargas
# Jun 02, 2022.
# The following tool, it helps to move
# and rename HEIC, JPG, JPEG, DNG or PNG files
# to a new directory location.
# Note: Automating task.

# Modules used in this program.
import shutil
import os

# main fuction controls working flow of
# this program.
def main() -> None:
    clear_screen()
    print("\n\n\n\tLet's move and rename pix *- Returns -* to raw materials files...\n\n")
    src_path, target_path, dir_name = working_dirs()
    
    make_dir(target_path,dir_name)

    os.chdir(src_path)
    print(os.getcwd())
    files = os.listdir(src_path)

    move_and_rename(files, target_path, dir_name)

# This function sets up working directories.
def working_dirs() -> str:
    home_path = os.path.expanduser('~')
    src_path =  home_path + '/Downloads'
    target_path = home_path + '/Documents/Returns/'
    dir_name = dir_file_name()

    return src_path, target_path, dir_name

# Iterate through source dir list, get, and move files with new names
# to new destination.    
def move_and_rename(files, target_path, dir_name):
    ext = '.DNG' # Setting file extension
    slash = '/' # delimiter
    delimiter = '-' # delimiter
    prefix = 1 # as starter counter. 
    for file in files:
        if file.endswith(('.HEIC','.PNG','.DNG','.JPG'), 7):
            shutil.move(file, target_path + dir_name + slash +
                        str(prefix) + delimiter + dir_name + ext)
            print(file)
            prefix += 1

# Creating destination directory.
def make_dir(target_path, dir_name) -> None:
    os.mkdir(target_path + dir_name)

# Promting user for directory name and return the name.
def dir_file_name() -> str:
    file_name = input("Enter directory / file name: ")
    return file_name

# Note: For unix like system: os.system("clear")
#       windows OS: os.system("cls")
def clear_screen() -> None:
    os.system("clear")

# Starting point of program.
# main() call.
if __name__ == '__main__':
    main()