from flask import Flask
from flask import request
from flask import render_template

import urllib.parse
import urllib.request
import json as m_json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/', methods=['POST'])
def books():
    mytitle = request.form['title']
    myauthor = request.form['author']
    book_list = recommended(mytitle, myauthor)
    return book_list

def recommended(title, author):
    your_book = "You enjoyed " + title.upper() + ", by " + author.upper() + ". \n"
    return your_book + "You may also enjoy: \n" + search_author(author)

def search_author(query):
    query += ' books'
    query = urllib.parse.urlencode ( { 'q' : query } )
    response = urllib.request.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query).read()
    json = m_json.loads ( response.decode('utf8') )
    results = json [ 'responseData' ] [ 'results' ]
    answers = ""

    for result in results:
        title = result['title']
        url = result['url']
        answers += title + ", "

    return answers

if __name__ == '__main__':
    app.run(debug=True)
