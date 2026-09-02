import os

# from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# evidence
evidence = ["Blue Cap","Necklace","Socks","Nail","Key"]

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/guess", methods=["GET", "POST"])
def guess():
    # when user makes a guess about the riddle, return template based on response 
    if request.method == "POST":
        answer = request.form.get('check')
        print(answer)
        if answer == "rubber duck":
            return render_template("guess.html",evidence=evidence)
        else:
            return render_template("retry.html",message="Wrong! Try again")

@app.route("/check", methods=["GET", "POST"])
def check():
    # when user makes a guess about the suspect, return template based on response 
    if request.method == "POST":
        answer = request.form.get('check1')
        if answer == "Brian" or answer == "brian":
            return render_template("win.html")
        else:
            return render_template("guess.html",evidence=evidence,message="Wrong. Try again")




