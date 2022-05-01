from flask import Flask, render_template, request
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

ml_model = pickle.load(open('test_model.pkl', 'rb'))

def punctuation_removal(text):
    all_list = [char for char in text if char not in string.punctuation]
    clean_str = ''.join(all_list)
    return clean_str

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def fake_or_real():
    # retrieve user input 
    article = str(request.form["text"])
    # prepare data for machine model with NLP preprossesing
    prepped_art = punctuation_removal(article)
    tok_article = word_tokenize(prepped_art)
    stop_words = stopwords.words('english')
    cleaned_article = " ".join([word for word in tok_article if word not in stop_words])
    # machine learning model and render results
    prediction = ml_model.predict([cleaned_article])
    if prediction[0] == "true":
        output = "looks CREDIBLE!"
    else:
        output = "looks like FAKE NEWS!"
    return render_template('index.html', prediction_text="Your article looks {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)