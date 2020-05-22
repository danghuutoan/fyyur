from startup.app import app
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort


@app.route('/')
def index():
    return render_template('pages/home.html')
