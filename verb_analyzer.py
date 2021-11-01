import re
import os
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import json

redundancy_list = ["wa", "would", "said", "would", "got", "let", "told", "could", "got", "says", "say", "want", "see",
                   "done", "get", "set", "ha", "put", "goes", "goe", "went", "ad"]

MF_dict = {}
word_bag = []


def get_verbs_from_file(path):
    verbs = []
    porter = PorterStemmer()
    dir = r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\pos"
    os.chdir(dir)
    with open(path, encoding="utf-8") as openfile:
        for line in openfile:
            for part in line.split('.'):
                if "he " in part:
                    line = part.split()
                    for i in range(len(line)-1):
                        if line[i] == "he":
                            word = re.sub(r'\W', '', porter.stem(line[i+1]))
                            word = re.sub(r'\s+', ' ', word, flags=re.I)
                            verbs.append(word.strip("_"))
    openfile.close()
    return verbs


def removing_stop_words(listyu):
    stop_words = set(stopwords.words('english'))
    redundancy_list.extend(stop_words)
    for i in range(len(listyu)):
        for stop in redundancy_list:
            if listyu[i] == stop:
                listyu[i] = ""

    new_list = [word for word in listyu if word != ""]
    return new_list


def collect_verbs(path):
    verbs = get_verbs_from_file(path)
    filtered_list = removing_stop_words(verbs)
    for word in filtered_list:
        MF_dict[word] = MF_dict.get(word, 0) + 1

    key_list = MF_dict.keys()
    keys_2_del = []

    for word in key_list:
        temp = word + "ed"
        if temp in MF_dict.keys():
            MF_dict[word] += MF_dict[temp]
            keys_2_del.append(temp)

    for key in keys_2_del:
        del MF_dict[key]

    too_small =[]
    for word in MF_dict.keys():
        if MF_dict[word]<5:
            too_small.append(word)

    for key in too_small:
        del MF_dict[key]


def get_all(path):
    path_list = os.listdir(path)
    for path in path_list:
        collect_verbs(path)


# get_all(r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\pos")
# # for key, value in sorted(MF_dict.items(), key=lambda item: item[1]):
# #     print(key, value)
# with open(r'C:\Users\b_sch\PycharmProjects\bookDownloader\result-pos-he.json', 'w') as fp:
#     json.dump(MF_dict, fp)

 # getting the 6 highest corrolated results:
print("pos")
get_all(r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\pos")

for key, value in sorted(MF_dict.items(), key=lambda item: item[1]):
    print(key, value)

# print("neg")
# get_all(r"C:\Users\b_sch\OneDrive\Documents\computerScience\gender based\bookDataBase\neg")
#
# for key, value in sorted(MF_dict.items(), key=lambda item: item[1]):
#     print(key, value)
