from flask import Flask

app = Flask(__name__)

@app.get("/hello/<user>")
def hello_world(user: str):
    return f"<p>Hello, {user}!</p>"

@app.get("/")
def index():
    return app.redirect("/hello/world")
