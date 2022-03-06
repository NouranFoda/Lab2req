from flask import Flask, render_template, request

# TODO: create new Flask app
app=Flask(__name__)

users=[ 
    { 
        "email":"nouran2000.foda@gmail.com",
        "username":"Nouran",
        "password":123
    },
    {
        "email":"farouha.shawky@gmail.com",
        "username":"Farah",
        "password":1234
    }
]

def sign_up():
    # TODO: get user input from request
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
   
    if not user_exists(email=email, username=username, password=password):
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"

def user_exists(email, username, password):
    for user in users:
        if (user["email"]==email and user["username"]==username):
            return True
    return False

@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template("index.html")
    
# TODO: Add route for sign up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    return sign_up()
   #Modification here after cloning (modify 2)
    

app.run(debug=True)




