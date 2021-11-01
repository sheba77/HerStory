from flask import Flask, json, send_from_directory, request, url_for
import json
import words_2_vec
import os

print('>>>' + __name__)
app = Flask(__name__)

@app.route('/')
def main_html():
    return send_from_directory('templates', 'main.html')


@app.route('/books',  methods=['GET'])
def get_books():
    with open(r"C:\Users\b_sch\PycharmProjects\HerStory\all_books_dict") as json_file:
        books = json.load(json_file)
    return json.dumps(books)


@app.route('/books',  methods=['POST'])
def check_book():
    book_path_string = request.data
    print(book_path_string)
    book_name = str(book_path_string).split(os.sep)[-1].strip("'")
    new_book_path_string = os.path.join(r"C:\Users\b_sch\PycharmProjects\HerStory\book2try", book_name)
    #book_path = os.path.normpath(new_book_path_string)
    per, fem = words_2_vec.out_side_test(new_book_path_string)
    result = {"percentage": per, "is_feminist": fem.item()}
    return json.dumps(result)


@app.route('/css/index.css')
def send_css():
    return send_from_directory(r'static\css', 'index.css')


@app.route('/css/img/bg.jpeg')
def send_bg_image():
    return send_from_directory(r'static\css\img', 'bg.jpeg')


if __name__ == "__main__":
    app.run(debug=True)

