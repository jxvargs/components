#!/usr/bin/env python3

# JVargas
# Jun 02, 2022.
# The following tool, it helps to move
# and rename HEIC, JPG, JPEG, DNG or PNG files
# to a new directory location.
# Note: Automating task.

# Modules used in this program.
import shutil
import os, time

# main fuction controls work flow of
# the program.
def main() -> None:
    clear_screen()
    print("\n\n\n\tLet's move and rename pix *- Returns -* to raw materials directory...\n\n\n")

    dir_file_name()

# Promting user for directory name and return the name.
def dir_file_name() -> str:
    blank = ''
    while True:
        file_name = input("Enter WO # or 'q' to QUIT: ")
        if file_name.lower() == 'q':
        # Exit with status value os.EX_OK
        # Utilizing os._exit passing parameter (os.EX_OK)
        # value of os.EX_OK is 0
            print('\n\tBye ', end='')
            for i in range(5):
                print(".", end='', flush= True)
                time.sleep(0.5)
            print('\n')
            os._exit(os.EX_OK)
        elif file_name == blank:
            print("\n\tWrong entry -*-BLANKS-*- are not allowed...\n")
            continue
        else:
           print("\tDone...\n")
           make_dir(file_name)

# if destination directory does not exist then create it.
# if destination exist then move files into it.
def make_dir(file_name) -> None:
    home_dir = os.environ.get('HOME')
    location = 'Downloads'
    destination = os.path.join('Documents', 'Returns')
    target_dir = os.path.join(home_dir, destination, file_name)
    target_path = os.path.join(home_dir, destination)
    print("\n\n\tDestination directory...")
    print(f"\n\n\t{target_dir}\n\n")
    src_dir = os.path.join(home_dir, location)

    if os.path.exists(target_dir) and os.path.isdir(target_dir):
        move_to_existing_dir(target_dir, src_dir, file_name) ###
    else:
        os.mkdir(target_dir)
        move_and_rename(target_path, file_name, src_dir)

def move_to_existing_dir(target_dir, src_dir, file_name) -> None:
    extension, ext_option, delimiter = extensions()
    files_to_move = []
    os.chdir(src_dir)
    files = os.listdir(src_dir)
    for file in files:
        if file.endswith(ext_option, 7):
            files_to_move.append(file)
            print(file)
            time.sleep(2)
    print('\n')

    files = os.listdir(target_dir)
    prefix = len(files) + 1
    print("Moving files:")
    print("--------------")
    for file in files_to_move:
        shutil.move(file, os.path.join(target_dir, str(prefix) + delimiter + file_name + extension))
        prefix += 1

# It iterates through source directory list gets, and moves files 
# from source directory with new names to new destination.
# Note: Alternate options:
#      1- home_path = os.path.expanduser('~')
#      2- home_path = os.envorion.get('HOME')    
def move_and_rename(target_path, dir_name, src_dir) -> None:
    extension, ext_option, delimiter = extensions()
    print("\n\tChanging directory to /Downloads...\n")
    time.sleep(2) # Suspending execution to change directory
    os.chdir(src_dir)
    files = os.listdir(src_dir)
    prefix = 1 # Counter as part of the file_name
    print("Moving files:")
    print("-------------")
    for file in files:
        if file.endswith(ext_option, 7):
            shutil.move(file, os.path.join(target_path, dir_name, str(prefix) +  
                   delimiter + dir_name + extension))
            print(file)
            time.sleep(0.5)
            prefix += 1
    print('\n')

def extensions() -> str:
    extension = '.DNG' # Setting file extension
    ext_option = ('.HEIC','.PNG','.DNG','.JPG', '.jpg', 'jpeg', 'JPEG', 'png')
    delimiter = '-' # delimiter
   
    return extension, ext_option, delimiter

# Note: For unix like system: os.system("clear")
#       windows OS: os.system("cls")
def clear_screen() -> None:
    os.system("clear")

# Starting point of program.
# main() call.
if __name__ == '__main__':
    main()