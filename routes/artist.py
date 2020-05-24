from startup.app import app
from models.city import City
from models.artist import Artist
from models.genre import Genre
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
from datetime import datetime
from forms import ArtistForm
from startup.db import db
import sys
#  Artists
#  ----------------------------------------------------------------


@app.route('/artists')
def artists():
    # TODO: replace with real data returned from querying the database
    artists = Artist.query.order_by(Artist.id).all()
    return render_template('pages/artists.html', artists=artists)


@app.route('/artists/search', methods=['POST'])
def search_artists():
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
    # search for "band" should return "The Wild Sax Band".
    response = {
        "count": 1,
        "data": [{
            "id": 4,
            "name": "Guns N Petals",
            "num_upcoming_shows": 0,
        }]
    }
    return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):

    artist = Artist.query.get(artist_id)
    now = datetime.now()
    past_shows = []
    upcoming_shows = []

    for show in artist.shows:
        if show.start_time < now:
            past_shows.append({"venue_id": show.venue.id,
                               "venue_name": show.venue.name,
                               "venue_image_link": show.venue.image_link,
                               "start_time": show.start_time.isoformat()})
        else:
            upcoming_shows.append({"venue_id": show.venue.id,
                                   "venue_name": show.venue.name,
                                   "venue_image_link": show.venue.image_link,
                                   "start_time": show.start_time.isoformat()})

    genres = []
    for genre in artist.genres:
        genres.append(genre.name)

    data = {
        "id": artist.id,
        "name": artist.name,
        "genres": genres,
        "city": artist.city.name,
        "state": artist.city.state.name,
        "phone": artist.phone,
        "seeking_venue": artist.seeking_venue,
        "facebook_link": artist.facebook_link,
        "website": artist.website,
        "seeking_description": artist.seeking_description,
        "image_link": artist.image_link,
        "past_shows": past_shows,
        "past_shows_count": len(past_shows),
        "upcoming_shows": upcoming_shows,
        "upcoming_shows_count": len(upcoming_shows)
    }
    return render_template('pages/show_artist.html', artist=data)

#  Update
#  ----------------------------------------------------------------


@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
    artist = Artist.query.get(artist_id)
    form = ArtistForm(genres=[2], name=artist.name,
                      phone=artist.phone, city=artist.city.name, state=artist.city.state.name, facebook_link=artist.facebook_link)

    return render_template('forms/edit_artist.html', form=form, artist=artist)


@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
    error = None
    try:
        app.logger.info(request.get_json())
        body = {}
        artist = Artist.query.get(artist_id)
        if artist == None:
            return abort(404)
        artist_name = request.get_json()['name']
        city_name = request.get_json()['city']
        state_id = request.get_json()['state']
        genres = request.get_json()['genres']

        artist.name = artist_name
        city = City.query.filter(City.name == city_name).first()

        if city == None:
            city = City(name=city_name)
            city.state_id = state_id
            # db.session.add(city)
            # db.session.commit()

        artist.city = city
        artist.phone = request.get_json()['phone']
        artist.facebook_link = request.get_json()['facebook_link']

        artist.genres = []
        for genre_id in genres:
            genre = Genre.query.get(genre_id)
            artist.genres.append(genre)

        db.session.add(artist)
        db.session.commit()
        app.logger.debug(artist)
        body['id'] = artist.id
        body['name'] = artist.name
    except:
        error = True
        app.logger.debug(sys.exc_info())
        db.session.rollback()

    finally:
        db.session.close()

    if error:
        flash('Artist ' + artist_name + ' could not be updated.')

        abort(400)
    else:
        flash('Artist ' + artist_name + ' was successfully updated!')
        return jsonify(body)


@ app.route('/artists/create', methods=['GET'])
def create_artist_form():
    form = ArtistForm()
    return render_template('forms/new_artist.html', form=form)


@ app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    error = False
    try:
        app.logger.info(request.get_json())
        body = {}
        artist = Artist(name=request.get_json()['name'])
        city_name = request.get_json()['city']
        state_id = request.get_json()['state']
        genres = request.get_json()['genres']
        city = City.query.filter(City.name == city_name).first()

        if city == None:
            city = City(name=city_name)
            city.state_id = state_id
            db.session.add(city)
            db.session.commit()

        artist.city_id = city.id
        artist.phone = request.get_json()['phone']
        artist.facebook_link = request.get_json()['facebook_link']

        for genre_id in genres:
            genre = Genre.query.get(genre_id)
            artist.genres.append(genre)
        db.session.add(artist)
        db.session.commit()
        body['id'] = artist.id
        body['name'] = artist.name

    except:
        print("Oops!", sys.exc_info(), "occured.")
        error = True
        db.session.rollback()

    finally:
        db.session.close()

    if error:
        flash('Artist ' + artist.name + ' could not be listed.')
        abort(400)
    else:
        flash('Artist ' + artist.name + ' was successfully listed!')
        return jsonify(body)
