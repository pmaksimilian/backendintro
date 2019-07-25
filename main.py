from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():

    name = "Maks"
    current_year = datetime.datetime.now().year

    return render_template("index.html",
                           name=name,
                           current_year=current_year)


@app.route("/about")
def about():

    previous_jobs = ["Prodajalec", "Kuhar", "Natakar", "Asistent"]

    return render_template("about.html", previous_jobs=previous_jobs)


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run(debug=True)
