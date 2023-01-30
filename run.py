import os 
import json
#import flask class
from flask import Flask, render_template, request


#creating instance of flask class and storing in variable "app"
#first argument for the flask class is the "name"
app = Flask(__name__)

#app.route decorator - way of wrapping functions 
@app.route("/")
def index():
    return render_template("index.html")

#route decorator, will pass data from the url path into the view below
@app.route("/about/<member_name>")
#member_name taken from above as an argument
def about_member(member_name):
    #member will store data in for later, open company.json file as read only
    member = {}
    with open("data/company.json", "r") as json_data:
        # then we pass through data that we have pulled and converted into json.
        data = json.load(json_data)
        # iterate through data array
        for obj in data:
            # check if object url key is equal to name passed through url path.
            if obj["url"] == member_name:
                #if they do match we want our empty member{} to be equal to the object in this loop instance.
                member = obj
    #click up heading titles in about page leads you to new page
    #with first member refering to member.html, second member is member object created about.
    return render_template("member.html", member=member)

#creating a route where the path is "/about"
@app.route("/about")
def about():
    data = []
    #python needs to open the json file and "r" its a read only file.
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print(request.form.get("name"))
        print(request.form["email"])
        #how to access data from the backend of our site
    return render_template("contact.html", page_title="Contact")


#
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