'''
                                       _
  ___ ___  _ __ ___  _ __   __ _ _ __ (_) ___  _ __
 / __/ _ \| '_ ` _ \| '_ \ / _` | '_ \| |/ _ \| '_ \
| (_| (_) | | | | | | |_) | (_| | | | | | (_) | | | |
 \___\___/|_| |_| |_| .__/ \__,_|_| |_|_|\___/|_| |_|
                    |_|


2025 wookieware..

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__email__ = "rick@rickkauffman.com"
__status__ = "Alpha"

COMPANION is a flask application to perform C.R.U.D. actions on the new version of Aruba Central
HTTP GEt, POST, DELETE, And PUT are demonstrated.

'''
from flask import Flask, request, render_template, abort, redirect, url_for
import pymongo
import datetime
import os
from bson.json_util import dumps
from bson.json_util import loads
from werkzeug.utils import secure_filename
import uuid
from jinja2 import Environment, FileSystemLoader
from utility.get_client_api import get_client
from utility.api_caller import api_caller

#
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_TEMPLATE = os.path.join(APP_ROOT, 'templates')

config = {
    "username": "admin",
    "password": "siesta3",
    "server": "mongo",
}
# mongodump --uri="mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = pymongo.MongoClient(connector)
db = client["demo"]
'''
#-------------------------------------------------------------------------------
Login and Test Page Section
#-------------------------------------------------------------------------------
'''

@app.route("/")
def main():
    return render_template('login.html')

@app.route("/test")
def test():
    return render_template('test_table.html')

@app.route("/login", methods=('GET', 'POST'))
def login():
    return render_template('login.html')
'''
#-------------------------------------------------------------------------------
Logout
#-------------------------------------------------------------------------------
'''

@app.route("/logout", methods=('GET', 'POST'))
def logout():
    # Check user credentials
    return render_template('logout.html')

'''
#-------------------------------------------------------------------------------
Home and Home_again
#-------------------------------------------------------------------------------
'''

@app.route("/home", methods=('GET', 'POST'))
def home():
        # Go home
        message = 'System Operation Normal'
        return render_template('home.html', message=message)

@app.route("/home_again", methods=('GET', 'POST'))
def home_again():
    # Check user credentials.
    message = 'System Operation Normal'
    # return
    return render_template('home.html', message=message)

'''
#-------------------------------------------------------------------------------
Log Section
#-------------------------------------------------------------------------------
'''

@app.route("/get_sites", methods=('GET', 'POST'))
def get_sites():
    client = get_client()

    api_method = "GET"

    api_path="network-config/v1alpha1/sites"

    sites = api_caller(client,api_method,api_path)

    # Check user credentials
    return render_template('get_sites.html', sites=sites)

@app.route("/create_site", methods=('GET', 'POST'))
def create_site():
    # Get a list of Actions

    # Check user credentials
    return render_template('create_site.html')

@app.route("/add_site", methods=('GET', 'POST'))
def add_site():
    # Get a list of Actions

    # Check user credentials
    return render_template('add_site.html')

@app.route("/update_site", methods=('GET', 'POST'))
def update_site():
    # This is the site chooser

    # Get list of sites and make a list of the names

    return render_template('update_site.html')


@app.route("/delete_site", methods=('GET', 'POST'))
def delete_site():

    return render_template('delete_site.html')
