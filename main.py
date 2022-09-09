from flask import Flask, render_template

app = Flask(__name__) # creating instance of flask

## HOME PAGE
@app.route("/") # @ is decorator
def home_page():
    return render_template("home.html")


## DYNAMIC USER NAME
# {} ginger formating
@app.route("/<name>") # @ is decorator
def user(name):
    # return f"This is {name}"
    return render_template("home.html", username = name)


## INFO PAGE
@app.route("/info")
def info_page():
    return render_template("info.html")


## CONTACT PAGE
@app.route("/contact")
def contact_page():
    return render_template("contact.html")





app.run()



