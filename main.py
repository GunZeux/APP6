from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def domain():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    return {"station": station,
            "date": date}


if __name__ == "__main__":
    app.run(debug=True)
