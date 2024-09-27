from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)

station_file = "data/stations.txt"
stations = pd.read_csv(station_file, skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
@app.route("/home")
def domain():
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}


@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    df["    DATE"] = df["    DATE"].astype(str)
    temperature = df.loc[df["    DATE"].str.startswith(str(year))]
    result = temperature.to_dict(orient="records")
    return result


@app.route("/api/v1/<station>")
def a_station(station):
    filename = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20)
    result = df.to_dict(orient="records")
    return result


if __name__ == "__main__":
    app.run(debug=True)
