from flask import Flask, json, send_from_directory, request, url_for
import json
import words_2_vec
import os

print('>>>' + __name__)
app = Flask(__name__)
dir_name = os.path.dirname(__file__)

@app.route('/')
def main_html():
    return send_from_directory('templates', 'main.html')

##
# This function gets called at start up of the local web page, and takes all the books
# we can choose from and places them into a jason file to read from
##
@app.route('/books',  methods=['GET'])
def get_books():
    file_name = os.path.join(dir_name, "all_books_dict")
    with open(file_name) as json_file:
        books = json.load(json_file)
    return json.dumps(books)


##
# creates a path to the wanted book, calls on words_2_vec class to train and create the
# model and then receives the results which is a tuple of percentage and a boolean of
# if the book is feminist or not.
##
@app.route('/books',  methods=['POST'])
def check_book():
    book_path_string = request.data
    book_name = str(book_path_string).split(os.sep)[-1].strip("'")
    book_path = os.path.join(dir_name, "book2try", book_name)
    per, fem = words_2_vec.out_side_test(book_path)
    result = {"percentage": per, "is_feminist": fem.item()}
    return json.dumps(result)

##
# send file to show on local web page
##
@app.route('/css/index.css')
def send_css():
    return send_from_directory(r'static\css', 'index.css')


@app.route('/css/img/bg.jpeg')
def send_bg_image():
    return send_from_directory(r'static\css\img', 'bg.jpeg')


if __name__ == "__main__":
    app.run(debug=True)

