from flask import (Flask, flash, request, redirect, render_template, url_for, session)
from flask.ext.script import Manager
from rauth.service import OAuth2Service

app = Flask(__name__)
manager = Manager(app)

facebook = OAuth2Service(
  name="facebook",
  base_url="https://graph.facebook.com/",
  access_token_url="https://graph.facebook.com/oauth/access_token",
  authorize_url="https://www.facebook.com/dialog/oauth",
  client_id="770624836357224",
  client_secret="28a5c399b2aeeb8c3b0105ab32b60674"
)

@app.route("/")
def index():
  return render_template("login.html")

if __name__ == "__main__":
  manager.run()
