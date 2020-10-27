from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello, World!'
    return render_template("home.html")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST": # POST "hides" data in request instead of pass to URL in GET method

        # Uncomment the two line below to test form data is passed correctly
        # req = request.form
        # print("Username is", req.get("username"))
        return redirect(request.url)

    return render_template("signup.html")


    
if __name__ == "__main__":
    app.run()