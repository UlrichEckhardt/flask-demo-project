from flask import Flask
from . import app

@app.get("/hello/<user>")
def hello_world(user: str):
    return f"<p>Hello, {user}!</p>"

@app.get("/")
def index():
    return app.redirect("/hello/world")

@app.get("/favicon.ico")
def favicon():
    return app.send_static_file("icons/favicon.ico")
