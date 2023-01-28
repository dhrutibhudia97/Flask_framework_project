import os 
#import flask class
from flask import Flask, render_template

#creating instance of flask class and storing in variable "app"
#first argument for the flask class is the "name"
app = Flask(__name__)

#app.route decorator - way of wrapping functions 
@app.route("/")
def index():
    return render_template("index.html")


#creating a route where the path is "/about"
@app.route("/about")
def about():
    return render_template("about.html", page_title="About")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


#settings arguments for the the app
#debug=True allows easier debugging at later stages
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# NEVER HAVE DEBUG=TRUE WHEN WE SUBMIT PROJECT UP FOR ASSESSMENT