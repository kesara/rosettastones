##############################################################################
# app.py
# Rosetta Stones Web Application
# 
# Copyright (C) Kesara Rathnayake
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

from flask import Flask, render_template

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
