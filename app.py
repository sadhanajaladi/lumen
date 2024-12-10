from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET"])
def homepage():
    return "<h1>Hello CodeWala :)</h1>"