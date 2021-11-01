import json


def get_file_names(path):
    small_dict={}
    path_name = path[0:]
    from os import listdir
    from os.path import isfile, join
    for f in listdir(path):
        if isfile(join(path, f)):
            pretty_name = f.strip(".txt").replace("-", " ").capitalize()
            small_dict[pretty_name] = path_name + "\\" + f
    return small_dict


file_dict = {}
# file_dict.update(get_file_names(r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\pos"))
# file_dict.update(get_file_names(r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\neg"))
file_dict.update(get_file_names(r"C:\Users\b_sch\PycharmProjects\HerStory\book2try"))

with open("all_books_dict", "w") as fp:
    json.dump(file_dict, fp)
