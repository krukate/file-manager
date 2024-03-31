import os
import shutil


def make_file(file_name):
    my_file = open(file_name, "w")
    my_file.close()


def remove_file(file_name):
    os.remove(file_name)


def add_text(file_name, text):
    with open(file_name, "a") as my_file:
        my_file.write(text)


def read_file(file_name):
    with open(file_name, "r") as my_file:
        print(my_file.read())


def copy_file(file_name, dir1, dir2):
    shutil.copy(os.path.join(dir1, file_name), dir2)


def move_file(file_name, dir1, dir2):
    shutil.move(os.path.join(dir1, file_name), dir2)


def rename_file(file_name, file_name2):
    os.rename(file_name, file_name2)
