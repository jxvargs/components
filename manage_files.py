#!/usr/bin/env python3

# JVargas
# Jun 02, 2022.
# The following tool, it helps to move
# and rename HEIC, JPG, JPEG, DNG or PNG files
# to a new directory location.
# Note: Automating task.

# Modules used in this program.
from distutils import extension
import shutil
import os

# main fuction controls working flow of
# this program.
def main() -> None:
    clear_screen()
    print("\n\n\n\tLet's move and rename pix *- Returns -* to raw materials files...\n\n")

    dir_name = dir_file_name()
    src_path, target_path = working_dirs()
    
    make_dir(target_path,dir_name)

    os.chdir(src_path)
    print(os.getcwd())
    files = os.listdir(src_path)

    move_and_rename(files, target_path, dir_name)

# This function sets up working directories.
# Note: Alternate options:
#      1- home_path = os.path.expanduser('~')
#      2- home_path = os.envorion.get('HOME') 
def working_dirs() -> str:
    home_path = os.environ.get('HOME')
    src_path =  os.path.join(home_path, 'Downloads')
    target_path = os.path.join(home_path, 'Documents/Returns')

    return src_path, target_path

# It iterates through source directory list gets, and moves files 
# from source directory with new names to new destination.    
def move_and_rename(files, target_path, dir_name):
    extension = '.DNG' # Setting file extension
    extensions = ('.HEIC','.PNG','.DNG','.JPG', '.jpg', 'png')
    delimiter = '-' # delimiter
    prefix = 1 # as starter counter. 
    for file in files:
        if file.endswith(extensions, 7):
            shutil.move(file, os.path.join(target_path, dir_name, str(prefix) +  
                   delimiter + dir_name + extension))
            print(file)
            prefix += 1

# Creating destination directory.
def make_dir(target_path, dir_name) -> None:
    os.mkdir(os.path.join(target_path, dir_name))

# Promting user for directory name and return the name.
def dir_file_name() -> str:
    active = True
    blank = ''
    while active:
        file_name = input("Enter WO # or 'q' to QUIT: ")
        if file_name.lower() == 'q':
        # Exit with status value os.EX_OK
        # Utilizing os._exit passing parameter (os.EX_OK)
        # value of os.EX_OK is 0
            os._exit(os.EX_OK)
        elif file_name == blank:
            print("\n\tWrong entry -*-BLANKS-*- are not allowed...\n")
            continue
        else:
            return file_name

# Note: For unix like system: os.system("clear")
#       windows OS: os.system("cls")
def clear_screen() -> None:
    os.system("clear")

# Starting point of program.
# main() call.
if __name__ == '__main__':
    main()