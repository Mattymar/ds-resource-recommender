import flask
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import re
from nltk.stem.snowball import SnowballStemmer


stemmer = SnowballStemmer('english')

stopwords = nltk.corpus.stopwords.words('english')
stopwords.extend(['machine', 'data', 'science', 'scientist', 'like', '’s', "'s", 'we’ll', 'e', 'g', 'n', 'com', 'el', 'la', 'un', 'los', 'daniel',
                      'tim', 'de', 'en', 'gt', 'lt', 'et', 'posted', 'powered', 'click', 'age', 'style', 'al''video', 'university', 'x', 'https', 'nginx', 'forbidden',
                      'amp', '\theta', 'q', '\mathbb', '\right', '\log', '\left', 'w', '\mathcal', '\hat', 'k', 'l', '\lambda',
                      'year', 'would', "n't", 'post', 'see', 'new', 'look', 'day', 'number', 'thing', 'think', 'want', 'show',
                      'word', 'paper', 'know', '\frac'])
                  
def tokenize_and_stem(text):
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens                
                  

tfidf_vectorizer = TfidfVectorizer(max_df=0.65,
                                   min_df=10, stop_words=stopwords,
                                   use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1, 3))

#tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')
tfidf_matrix = joblib.load('tfidf_matrix.pkl')

app = flask.Flask(__name__)



@app.route("/")
def home_page():
    """
    Homepage: serve our visualization page, awesome.html
    """
    with open("index.html", 'r') as home_file:
        return home_file.read()


@app.route("/post_recommendations", methods=["POST"])
def recommend():
    """
    When A POST request with json data is made to this uri,
    Read the example from the json, predict probability and
    send it with a response
    """
    # Get decision score for our example that came with the request
    data = flask.request.json
    text = data["text"]

    # Put the result in a nice dict so we can send it as json
    results = {"text": text}
    return flask.jsonify(results)


app.run(host='0.0.0.0', debug=True)
