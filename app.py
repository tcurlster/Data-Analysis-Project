from flask import Flask, render_template, request
#import pickle

app = Flask(__name__)

#ml_model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def fake_or_real():
#     run formthrough machine learning model and render results
    article = str(request.form["text"])
    
#         prediction = ml_model.predict(encoding_function(article))
#           output = 
#         return render_template('index.html', prediction_text="Your article is: {}".format(output))
    
    return article


if __name__ == "__main__":
    app.run(debug=True)