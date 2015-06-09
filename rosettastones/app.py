##############################################################################
# app.py
# Rosetta Stones Web Application
# 
# Copyright (C) 2015 Kesara Rathnayake
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################

from flask import Flask, jsonify, render_template

from rosettastones.lib.engine import generate_keys, get_hash

app = Flask(__name__)

@app.route("/")
def index():
    """
    Home page
    """
    return render_template("index.html")

@app.route("/add")
def add():
    """
    Insert a message
    """
    return render_template("add.html")

@app.route("/gen_keys", methods=["GET",])
def generate():
    """
    Generate rosetta master key and public key
    """
    (pub_key, naked_master_key) = generate_keys()
    master_key_hex = get_hash(naked_master_key)
    return jsonify({
        "public_key": pub_key,
        "master_key": master_key_hex})
