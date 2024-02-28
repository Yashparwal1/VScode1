from flask import Flask, render_template
app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route("/")
def hello():
    # return "Hello world"
    return render_template("index.html")

@app.route("/yash")
def yash():
    return "yash"

@app.route("/about")
def about():
    name = "Yash"
    return render_template("about.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)