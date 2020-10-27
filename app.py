from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)

app.secret_key=b'1jb@9^$'

@app.route('/')
@app.route('/home')
def home():
    # return 'Hello, World!'
    return render_template("home.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST": # POST "hides" data in request instead of pass to URL in GET method

        # Uncomment the two line below to test form data is passed correctly
        request_data = request.form
        sugg_username = request_data.get("username")
        sugg_password = request_data.get("password")

        if sugg_username != "" and sugg_password != "":
            flash("Sign up accepted. Try logging in!")
            return redirect("home")
        else:
            return redirect(request.url)

    return render_template("signup.html")


    
if __name__ == "__main__":
    app.run()