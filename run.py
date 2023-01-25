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

#settings arguments for the the app
#debug=True allows easier debugging at later stages
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
# NEVER HAVE DEBUG=TRUE WHEN WE SUBMIT PROJECT UP FOR ASSESSMENT