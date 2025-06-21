from flask import Flask, render_template, request
from model import predict_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    if request.method == "POST":
        text = request.form.get("comment")
        if text:
            sentiment = predict_sentiment(text)
    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)
