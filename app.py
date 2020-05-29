#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json

import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from flask_moment import Moment

from startup.db import db, migrate
from startup.app import app

import logging
from logging import Formatter, FileHandler
# from flask_wtf import Form
# from forms import *

import sys
# models
from models.genre import Genre
from models.artist import Artist
from models.venue import Venue
from models.city import City
from models.state import State
from models.show import Show

# routes
from routes.venue import *
from routes.artist import *
from routes.show import *
from routes.error import *
from routes.home import *

from forms import *

moment = Moment(app)


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
