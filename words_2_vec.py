# open each file and make a vector out of it:
import os
import re
import json
from nltk.stem.porter import PorterStemmer
import numpy
import sys

#  0 = chovenistic book 1= feminst book!
feature ={"accept", "actual", "add", "added", "address", "admit", "advanc", "agre", "aint", "allow", "almost", "alon",
          "also", "alway", "announc", "answer", "appear", "approach", "aros", "arriv", "ascend", "ask", "assert", "ate",
          "avoid", "awok", "bade", "bear", "beat", "becam", "becom", "beg", "began", "begin", "begun", "beheld", "believ",
          "belong", "bends", "bent", "bestow", "bid", "big", "blows", "blush", "bore", "bought", "bow", "break",
          "breath", "bring", "broke", "brought", "call", "calld", "came", "cannot", "cant", "care", "carri", "cast",
          "caught", "certainli", "chanc", "chang", "check", "chose", "clap", "close", "come", "comes", "command",
          "commenc", "conceal", "conclud", "concluded", "consid", "continu", "couldnt", "cri", "cross", "crouch",
          "cut", "dare", "dead", "decid", "declar", "demand", "descend", "describ", "deserv", "desir", "determin",
          "didnt", "die", "died", "direct", "disappear", "discov", "doe", "doesnt", "dont", "doth", "drag", "drank",
          "drew", "drop", "drove", "emerg", "encount", "end", "endeavor", "enjoy", "enquir", "enter", "entertain",
          "even", "ever", "examin", "exclaim", "expect", "experienc", "explain", "express", "fall", "falls", "falter",
          "fanci", "fear", "feel", "fell", "felt", "figur", "find", "finish", "first", "fix", "fled", "flew", "fli",
          "flies", "flung", "follow", "forgot", "fought", "found", "frown", "gallop", "gasp", "gave", "gaze", "git",
          "give", "glanc", "glide", "go", "gon", "gone", "grasp", "grew", "grow", "hadnt", "haint", "halt", "hand",
          "hasten", "hate", "hath", "hear", "heard", "held", "hesit", "hi", "hold", "hope", "hum", "hurl", "imagin",
          "immedi", "implor", "inquir", "insist", "intend", "isnt", "judg", "jump", "keep", "kept", "kiss", "knew",
          "know", "laid", "laugh", "lay", "lean", "leant", "leap", "learn", "led", "left", "lie", "lies", "lift",
          "like", "linger", "listen", "live", "lock", "long", "look", "looks", "lost", "lovd", "love", "loved",
          "made", "make", "marri", "may", "mean", "meant", "medit", "mention", "met", "might", "mock", "motion",
          "mount", "move", "moved", "murmur", "muse", "mused", "must", "mutter", "near", "need", "never", "nod",
          "note", "notic", "observ", "offer", "often", "onc", "onli", "open", "order", "ought", "owe", "paid",
          "pass", "passd", "paus", "perceiv", "persist", "pick", "piti", "place", "play", "plead", "pleas", "plung",
          "point", "possess", "pour", "pray", "prefer", "present", "press", "proce", "proceed", "promis", "promisd",
          "pronounc", "propos", "protest", "pull", "push", "quit", "rais", "ran", "reach", "read", "realis", "realiz",
          "realli", "recal", "receiv", "reckon", "recogn", "recognis", "reflect", "regard", "rejoin", "remain",
          "remark", "rememb", "remind", "repeat", "repli", "requir", "resolv", "resum", "retort", "return", "risk",
          "roar", "rode", "rose", "rub", "rue", "rush", "sang", "sank", "sat", "sate", "saw", "scarc", "scream", "se",
          "seat", "seek", "seem", "seiz", "send", "sent", "shake", "shall", "shew", "shook", "shot", "shouldnt",
          "shout", "show", "shut", "sigh", "simpli", "sing", "sit", "sleep", "slept", "slept", "slew", "smile",
          "smote", "sold", "sometim", "soon", "sought", "spake", "speak", "speaks", "spent", "spoke", "sprang",
          "stand", "stands", "stare", "start", "stay", "step", "sternli", "still", "stood", "stop", "stretch",
          "strode", "struck", "stuck", "suddenli", "suffer", "suggest", "suppos", "swear", "swore", "take", "talk",
          "tell", "therefor", "think", "thinks", "thought", "threw", "thrust", "thu", "took", "tore", "touch", "travel",
          "trembl", "tri", "tumbl", "turn", "turnd", "understood", "use", "utter", "veri", "wait", "walk", "wander",
          "warnt", "wasnt", "watch", "wave", "wear", "weep", "wept", "wept", "whisper", "whose", "wish", "woke",
          "wonder", "wont", "wore", "work", "wouldnt", "write", "wrote", "may", "might", "never", "took"}

# all_data = []


from sklearn.datasets import load_files

my_data = load_files(r"C:\Users\b_sch\PycharmProjects\HerStory\bookDataBase")
path_2_books, y = my_data.data, my_data.target
target_array = y


def load_she(my_data):
    porter = PorterStemmer()
    books = []

    for path in my_data.filenames:
        with open(path, encoding="utf-8") as openfile:
            my_string = ""
            for line in openfile:
                for part in line.split('.'):
                    if "she " in part:
                        line = part.split()
                        for i in range(len(line) - 1):
                            if line[i] == "she":
                                word = re.sub(r'\W', '', porter.stem(line[i + 1]))
                                word = re.sub(r'\s+', ' ', word, flags=re.I)
                                my_string += word + " "
            books.append(my_string)
    return books

def load_he(my_data):
    porter = PorterStemmer()
    books = []

    for path in my_data.filenames:
        with open(path, encoding="utf-8") as openfile:
            my_string = ""
            for line in openfile:
                for part in line.split('.'):
                    if "he " in part:
                        line = part.split()
                        for i in range(len(line) - 1):
                            if line[i] == "he":
                                word = re.sub(r'\W', '', porter.stem(line[i + 1]))
                                word = re.sub(r'\s+', ' ', word, flags=re.I)
                                my_string += word + " "
            books.append(my_string)
    return books


def load_one(path):
    my_string = ""
    porter = PorterStemmer()

    with open(path, encoding="utf-8") as openfile:
        for line in openfile:
            for part in line.split('.'):
                if "she " in part:
                    line = part.split()
                    for i in range(len(line) - 1):
                        if line[i] == "she":
                            word = re.sub(r'\W', '', porter.stem(line[i + 1]))
                            word = re.sub(r'\s+', ' ', word, flags=re.I)
                            my_string += word + " "
    return [my_string]


def convert_2_vec(all_data):
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.feature_extraction.text import TfidfTransformer

    vectorizer = CountVectorizer(max_features=800, vocabulary=feature)
    X = vectorizer.fit_transform(all_data).toarray()

    tfidfconverter = TfidfTransformer()
    X = tfidfconverter.fit_transform(X).toarray()

    return X


# todo how to add the "he" to the mix
both_matrix = 0.5*convert_2_vec(load_she(my_data))+0.5*convert_2_vec(load_he(my_data))
# both_matrix = convert_2_vec(load_she(my_data))


def training_time():
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(both_matrix, target_array, test_size=0.2)

    from sklearn.neighbors import KNeighborsClassifier

    knn = KNeighborsClassifier(7)

    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    y_pro = knn.predict_proba(x_test)

    from sklearn import metrics
    # print(y_test)
    # print(y_pred)

    # import matplotlib.pyplot as plt
    # import scikitplot as skplt
    #
    # skplt.metrics.plot_roc(y_pred, target_array)
    # plt.show()


    # return metrics.accuracy_score(y_test, y_pred)

    return knn


def find_best_k():
#we want to find the best k to use: conclusion 7 is the best!!
    scoring = []
    count = 0
    while count <= 15:
        my_score = 0
        for i in range(2, 15):
            my_score += training_time()
        count += 1
        scoring.append(my_score)
    return scoring


# my_list = find_best_k()
# for k in range(len(my_list)):
#     print(k+2, my_list[k]/14)


def out_side_test(path):
    vec = convert_2_vec(load_one(path))
    knn = training_time()
    y_pred = knn.predict(vec)

    from sklearn.neighbors import NearestNeighbors
    x = knn.kneighbors_graph(vec)
    x.toarray()


    # print(knn.predict_proba(vec).tolist()[0][1])
    # print(y_pred[0])
    precent = knn.predict_proba(vec).tolist()[0][1]

    return precent, y_pred[0]


def conMatrix():
    path = r"C:\Users\b_sch\PycharmProjects\HerStory\testBooks"
    y_true = [1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0]
    y_pred = []

    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            # print(file)
            if '.txt' in file:
                per, res = out_side_test(os.path.join(r, file))
                y_pred.append(res)

    from sklearn.metrics import confusion_matrix
    print(confusion_matrix(y_true, y_pred))
    print(y_pred)


#conMatrix()
