#!/usr/bin/env python3

# JVargas
# Jun 02, 2022.
# The following tool, it helps to move
# and rename HEIC, JPG, JPEG, DNG or PNG files.
# Note: alpha development.

import shutil
import os

def main():
    clear_screen()
    print("\n\n\n\tLet's move and rename pix * Returns * to raw materials files...\n\n")
    src_path, target_path, dir_name = working_dirs()
    
    make_dir(target_path,dir_name)

    os.chdir(src_path)
    print(os.getcwd())
    files = os.listdir(src_path)

    move_and_rename(files, target_path, dir_name)

def working_dirs():
    home_path = os.path.expanduser('~')
    src_path =  home_path+ '/Downloads'
    target_path = home_path + '/Documents/Returns/'
    dir_name = dir_file_name()

    return src_path, target_path, dir_name
    
def move_and_rename(files, target_path, dir_name):
    prefix = 1
    for file in files:
        if file.endswith(('.HEIC','.PNG','.DNG','.JPG'), 7):
            shutil.move(file, target_path + dir_name + '/' +str(prefix) + '-' + dir_name + '.DNG')
            print(file)
            prefix += 1

def make_dir(target_path, dir_name) -> None:
    os.mkdir(target_path + dir_name)


def dir_file_name() -> str:
    file_name = input("Enter directory / file name: ")
    return file_name

def clear_screen() -> None:
    os.system("clear")


if __name__ == '__main__':
    main()