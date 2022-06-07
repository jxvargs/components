#!/usr/bin/env python3

# JVargas
# Jun 02, 2022.
# The following tool, it helps to move
# and rename HEIC, JPG, JPEG, DNG or PNG files.
# Note: alpha development.

import shutil
import os

def main():
    src_path = '/Users/ekbalam/Downloads'
    target_path = '/Users/ekbalam/Documents/Returns/' 
    
    clear_screen()

    print("\n\tLet's move and rename pix * Returns * raw materials files...\n")
    dir_name = dir_file_name()
    make_dir(dir_name)

    os.chdir(src_path)
    print(os.getcwd())
    files = os.listdir(src_path)

    move_and_rename(files)
    
def move_and_rename(files, dir_name, target_path):
    prefix = 1
    for file in files:
        if file.endswith(('.HEIC','.PNG','.DNG','.JPG'), 7):
            shutil.move(file, target_path+dir_name + '/' +str(prefix) + '-' + dir_name + '.DNG')
            print(file)
            prefix += 1

def make_dir(dir_name) -> None:
    os.mkdir(f'/Users/ekbalam/Documents/Returns/{dir_name}')


def dir_file_name() -> str:
    file_name = input("Enter directory / file name: ")
    return file_name

def clear_screen() -> None:
    os.system("clear")


if __name__ == '__main__':
    main()