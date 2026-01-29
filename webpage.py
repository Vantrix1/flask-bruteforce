from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

USERNAME= "admin"
PASSWORD= "matrix99"

@app.route("/",methods=["GET","POST"])
def login():
    print(app.url_map)

    if request.method == "POST":
        inputted_user = request.form.get("username")
        inputted_password = request.form.get("password")

        if inputted_user == USERNAME and inputted_password == PASSWORD:
            return "Credentials correct, successful login", 200
        else:
            return "Credentials incorrect, unsuccessful login", 401
    return render_template("login.html")
if __name__ == "__main__":
    app.run(debug=True)
