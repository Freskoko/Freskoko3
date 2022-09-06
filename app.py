from flask import Flask, redirect, render_template, request, url_for
import random

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))

def index():

    completedprompt = "Welcome"

    if request.method == "POST": 

        if "new" in request.form:

            completedprompt = generate_image()
        if "addplayerbutton" in request.form:
            completedprompt = addplayer()

        if "clear" in request.form:
            clear_names()
            completedprompt = "all names cleared!"
            
    return render_template("index.html", result=completedprompt)

def addplayer ():
    texttowrite = request.form['addplayer']
    with open("GameNames.txt","a") as file:
        if texttowrite != "":
            file.write(str(f"{texttowrite}\n"))
        file.close()

    return f"Welcome {texttowrite}"
    
def generate_image():

    with open("GameChallenges.txt","r") as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        funnytext = random.choice(lines)
        file.close()

    try:
        with open("GameNames.txt","r") as file:
            lines = file.readlines()
            lines = [line.rstrip() for line in lines]
            person = random.choice(lines)
            file.close()
    except Exception:
        return("⬇ No names... Add some below ⬇")

    return (f"{person} must {funnytext}")

def clear_names():
    with open("GameNames.txt","w") as file:
        file.close()