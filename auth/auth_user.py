from flask import Flask, session
from flask_bcrypt import Bcrypt

from auth.user_table import getUserByUsername

app = Flask(__name__)
bcrypt = Bcrypt(app)

def authUser(username, password):
    user = getUserByUsername(username)
    if user == None:
        return False
    if user and bcrypt.check_password_hash(user[2], password):
        session['logged_in'] = True
        session['username'] = username
        return True
    return False

