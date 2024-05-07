"""routing table"""
from datetime import datetime
from flask import render_template
from . import app


@app.get("/hello/<user>")
def hello_world(user: str):
    """render a greeting in HTML"""
    return render_template(
        "hello_world.html",
        name=user,
        date=datetime.now()
    )


@app.get("/")
def index():
    """default endpoint that redirects to the greeter"""
    return app.redirect("/hello/world")


@app.get("/favicon.ico")
def favicon():
    """favicon"""
    return app.send_static_file("icons/favicon.ico")
