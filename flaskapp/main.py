import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    appname = os.environ['APP_NAME']
    appversion = os.environ['APP_VERSION']

    response = "%s - %s.%s\n" %('HELLO WORLD FROM BERLIN', appname, appversion)
    return response