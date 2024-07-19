from flask import Flask, session
from flask_bcrypt import Bcrypt
import sqlite3

from auth.user_table import getUser
from config import SECRET_KEY

app = Flask(__name__)
bcrypt = Bcrypt(app)
def authUser(username, password):
    user = getUser(username)
    if user == None:
        return False
    if user and bcrypt.check_password_hash(user[2], password):
        session['logged_in'] = True
        session['username'] = username
        return True
    return False

