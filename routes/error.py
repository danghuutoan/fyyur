from startup.app import app
from flask import render_template, request, Response, flash, redirect, url_for, jsonify, abort


@ app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@ app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500

