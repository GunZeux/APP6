from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)
df = pd.read_csv("dictionary.csv")


@app.route("/")
@app.route("/home")
def home():
    return render_template("StudentHome.html")


@app.route("/api/v1/<word>")
def cap_word(word):
    data = {"definition": df.loc[df["word"] == word]["definition"].squeeze(),
            "word": word}
    return data


if __name__ == "__main__":
    app.run(debug=True)