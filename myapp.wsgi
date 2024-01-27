#!/usr/bin/env "/home/chris/Documents/Flask App 1/FlaskOne/env/bin/python3.11"

import sys

# Add the site-packages of the chosen virtualenv to work with
sys.path.append('/home/chris/Documents/Flask App 1/FlaskOne/env/lib/python3.11/site-packages')

sys.path.insert(0, '/home/chris/Documents/Flask App 1/FlaskOne')

from main import app as application