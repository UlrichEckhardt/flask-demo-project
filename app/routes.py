from datetime import datetime
from flask import Flask
from . import app

@app.get("/hello/<user>")
def hello_world(user: str):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    return f"Hello {user}! It's {formatted_now} now."

@app.get("/")
def index():
    return app.redirect("/hello/world")

@app.get("/favicon.ico")
def favicon():
    return app.send_static_file("icons/favicon.ico")
