import json
import os
dir_name = os.path.dirname(__file__)

##
# This function creates a dict that will hold {name of book: relative path to book}
##

def get_file_names(path):
    small_dict = {}
    path_name = path[0:]
    from os import listdir
    from os.path import isfile, join
    for f in listdir(path):
        if isfile(join(path, f)):
            pretty_name = f.strip(".txt").replace("-", " ").capitalize()
            small_dict[pretty_name] = path_name + "\\" + f
    return small_dict

##
# This file calls on previous function and updates the file called "all books dict".
# The commented out paths are for different databases files
##


def update_book_dict():
    file_dict = {}

    # file_dict.update(get_file_names(os.path.join(r"bookDataBase\pos")))
    # file_dict.update(get_file_names(os.path.join(r"bookDataBase\neg")))
    file_dict.update(get_file_names(os.path.join(r"book2try")))
    with open("all_books_dict", "w") as fp:
        json.dump(file_dict, fp)

update_book_dict()
