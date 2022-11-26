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
    print("\n\n\n\tLet's move and rename pix *- Returns -* to raw materials directory...\n\n\n")

    dir_file_name()

# It iterates through source directory list gets, and moves files 
# from source directory with new names to new destination.
# Note: Alternate options:
#      1- home_path = os.path.expanduser('~')
#      2- home_path = os.envorion.get('HOME')    
def move_and_rename(target_path, dir_name, src_dir):
    extension = '.DNG' # Setting file extension
    extensions = ('.HEIC','.PNG','.DNG','.JPG', '.jpg', 'jpeg', 'JPEG', 'png')
    delimiter = '-' # delimiter
    prefix = 1 # as starter counter.
    print(f"\n\tChanging directory to /Downloads...\n")
    os.chdir(src_dir)
    files = os.listdir(src_dir)
    for file in files:
        if file.endswith(extensions, 7):
            shutil.move(file, os.path.join(target_path, dir_name, str(prefix) +  
                   delimiter + dir_name + extension))
            print(file)
            prefix += 1
    print('\n')

# Creating destination directory.
# The following function setup working directories
def make_dir(file_name):
    home_path = os.environ.get('HOME')
    target_path = os.path.join(home_path, 'Documents/Returns')
    src_dir = os.path.join(home_path, 'Downloads')

    # Check if directory target exist <--
    
    os.mkdir(os.path.join(target_path, file_name))
    move_and_rename(target_path,file_name,src_dir)

# Checking existing of a directory
def dir_exist()

# Promting user for directory name and return the name.
def dir_file_name() -> str:
    blank = ''
    while True:
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
           print("\tDone...\n")
           make_dir(file_name)

# Note: For unix like system: os.system("clear")
#       windows OS: os.system("cls")
def clear_screen() -> None:
    os.system("clear")

# Starting point of program.
# main() call.
if __name__ == '__main__':
    main()