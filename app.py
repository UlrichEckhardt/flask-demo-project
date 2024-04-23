from flask import Flask

app = Flask(__name__, static_folder="static/")

@app.get("/hello/<user>")
def hello_world(user: str):
    return f"<p>Hello, {user}!</p>"

@app.get("/")
def index():
    return app.redirect("/hello/world")

@app.get("/favicon.ico")
def favicon():
    return app.send_static_file("icons/favicon.ico")
