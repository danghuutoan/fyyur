from startup.app import app
from startup.db import db
from models.show import Show
from models.artist import Artist
from models.venue import Venue
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from datetime import datetime
from forms import ShowForm
from utils.datetime import format_datetime


@ app.route('/shows')
def shows():
    # displays list of shows at /shows
    # TODO: replace with real venues data.
    #       num_shows should be aggregated based on number of upcoming shows per venue.
    shows = Show.query.filter(Show.start_time > datetime.now())
    data = []
    for show in shows:
        data.append({
            "venue_id": show.venue.id,
            "venue_name": show.venue.name,
            "artist_id": show.artist.id,
            "artist_name": show.artist.name,
            "artist_image_link": show.artist.image_link,
            "start_time": show.start_time.isoformat()
        })
    return render_template('pages/shows.html', shows=data)


@ app.route('/shows/create')
def create_shows():
    # renders form. do not touch.
    artist_choices = db.session.query(
        Artist.id, Artist.name).distinct().all()
    venue_choices = db.session.query(Venue.id, Venue.name).distinct().all()
    form = ShowForm(artist_choices, venue_choices)
    return render_template('forms/new_show.html', form=form)


@ app.route('/shows/create', methods=['POST'])
def create_show_submission():
    error = False
    try:
        artits_id = request.form.get('artist_id')
        venue_id = request.form.get('venue_id')
        start_time = request.form.get('start_time')
        show = Show()
        show.artist_id = artits_id
        show.venue_id = venue_id
        show.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
        db.session.add(show)
        db.session.commit()
    except:
        error = True
        db.session.rollback()
    finally:
        db.session.close()
    # called to create new shows in the db, upon submitting new show listing form
    # TODO: insert form data as a new Show record in the db, instead

    # on successful db insert, flash success
    if error == False:
        flash('Show was successfully listed!')
    else:
        flash('Show was failed listed!')
    # TODO: on unsuccessful db insert, flash an error instead.
    # e.g., flash('An error occurred. Show could not be listed.')
    # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
    return render_template('pages/home.html')
