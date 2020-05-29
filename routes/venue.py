from startup.app import app
from models.city import City
from models.venue import Venue
from models.genre import Genre
from models.show import Show
from datetime import datetime
from forms import VenueForm
from startup.db import db
import sys
from flask import Flask, render_template, request, Response, flash, redirect, url_for, jsonify, abort
#  Venues
#  ----------------------------------------------------------------


@app.route('/venues')
def venues():
    # TODO: replace with real venues data.
    #       num_shows should be aggregated based on number of upcoming shows per venue.

    cities = City.query.all()
    data = []
    for city in cities:
        if len(city.venues) > 0:
            data.append({
                'city': city.name,
                'state': city.state.name,
                'venues': city.venues
            })
    return render_template('pages/venues.html', areas=data)


@app.route('/venues/search', methods=['POST'])
def search_venues():

    search_term = "%{}%".format(request.form.get('search_term'))
    venues = Venue.query.filter(Venue.name.ilike(search_term)).all()
    # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
    # seach for Hop should return "The Musical Hop".
    # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
    data = []
    for venue in venues:
        up_comming_shows = Show.query.filter(Show.venue_id == venue.id,
                                             Show.start_time > datetime.now()).all()
        app.logger.debug(up_comming_shows)
        data.append({
            "id": venue.id,
            "name": venue.name,
            "num_upcoming_show": len(up_comming_shows)
        })

    response = {
        "count": len(data),
        "data": data
    }
    return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))


@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
    venue = Venue.query.get(venue_id)
    now = datetime.now()

    past_shows = []
    upcoming_shows = []

    for show in venue.shows:
        if show.start_time < now:
            past_shows.append({"artist_id": show.artist.id,
                               "artist_name": show.artist.name,
                               "artist_image_link": show.artist.image_link,
                               "start_time": show.start_time.isoformat()})
        else:
            upcoming_shows.append({"artist_id": show.artist.id,
                                   "artist_name": show.artist.name,
                                   "artist_image_link": show.artist.image_link,
                                   "start_time": show.start_time.isoformat()})
    genres = []
    for genre in venue.genres:
        genres.append(genre.name)

    data = {
        "id": venue.id,
        "name": venue.name,
        "genres": genres,
        "city": venue.city.name,
        "state": venue.city.state.name,
        "address": venue.address,
        "phone": venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "image_link": venue.image_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "past_shows": past_shows,
        "past_shows_count": len(past_shows),
        "upcoming_shows": upcoming_shows,
        "upcoming_shows_count": len(upcoming_shows)
    }
    return render_template('pages/show_venue.html', venue=data)

#  Create Venue
#  ----------------------------------------------------------------


@app.route('/venues/create', methods=['GET'])
def create_venue_form():
    form = VenueForm()
    return render_template('forms/update_venue.html', form=form, action="Create Venue")


@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
    error = False
    venue_name = request.get_json()['name']
    try:
        body = {}
        venue = Venue(name=venue_name)
        city_name = request.get_json()['city']
        state_id = request.get_json()['state']
        genres = request.get_json()['genres']
        city = City.query.filter(City.name == city_name).first()

        if city == None:
            city = City(name=city_name)
            city.state_id = state_id

        venue.city = city
        venue.phone = request.get_json()['phone']
        venue.facebook_link = request.get_json()['facebook_link']

        for genre_id in genres:
            genre = Genre.query.get(genre_id)
            venue.genres.append(genre)
        db.session.add(venue)
        db.session.commit()
        body['id'] = venue.id
        body['name'] = venue.name

    except:
        print("Oops!", sys.exc_info(), "occured.")
        error = True
        db.session.rollback()

    finally:
        db.session.close()

    if error:
        flash('venue ' + venue_name + ' could not be listed.')
        abort(400)
    else:
        flash('venue ' + venue_name + ' was successfully listed!')

    return jsonify(body)


@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
    app.logger.debug(f'delete {venue_id}')
    error = False
    body = {}
    try:
        # TODO: Complete this endpoint for taking a venue_id, and using
        # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.

        # BONUS CHALLENGE: Implement a button to delete a Venue on a Venue Page, have it so that
        # clicking that button delete it from the db then redirect the user to the homepage
        venue = Venue.query.get(venue_id)
        db.session.delete(venue)
        db.session.commit()
        body['id'] = venue.id
        body['name'] = venue.name
    except:
        db.session.rollback()
        error = True
    finally:
        db.session.close()

    if error:
        flash('Venue ' + venue.name + ' could not be deleted.')
        abort(400)
    else:
        flash('Artist ' + venue.name + ' was successfully deleted.')
        return jsonify(body)


@ app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):

    venue = Venue.query.get(venue_id)
    genres = []
    for genre in venue.genres:
        genres.append(genre.id)
    data = {
        "id": venue.id,
        "name": venue.name,
        "genres": genres,
        "address": venue.address,
        "city": venue.city.name,
        "state": venue.city.state.name,
        "phone": venue.phone,
        "website": venue.website,
        "facebook_link": venue.facebook_link,
        "seeking_talent": venue.seeking_talent,
        "seeking_description": venue.seeking_description,
        "image_link": venue.image_link
    }
    # app.logger.debug(genres)
    form = VenueForm(name=venue.name, genres=genres,
                     phone=venue.phone, city=venue.city.name, state=venue.city.state.id, address=venue.address, facebook_link=venue.facebook_link)
    # TODO: populate form with values from venue with ID <venue_id>
    return render_template('forms/update_venue.html', form=form, venue=data, action="Edit")


@ app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
    error = False
    venue_name = request.get_json()['name']
    try:
        app.logger.info(request.get_json())
        body = {}
        venue = Venue.query.get(venue_id)
        venue.name = venue_name
        city_name = request.get_json()['city']
        state_id = request.get_json()['state']
        genres = request.get_json()['genres']
        city = City.query.filter(City.name == city_name).first()

        if city == None:
            city = City(name=city_name)
            city.state_id = state_id
            db.session.add(city)
            db.session.commit()

        venue.city_id = city.id
        venue.phone = request.get_json()['phone']
        venue.facebook_link = request.get_json()['facebook_link']

        for genre_id in genres:
            genre = Genre.query.get(genre_id)
            venue.genres.append(genre)
        db.session.add(venue)
        db.session.commit()
        body['id'] = venue.id
        body['name'] = venue.name

    except:
        print("Oops!", sys.exc_info(), "occured.")
        error = True
        db.session.rollback()

    finally:
        db.session.close()

    if error:
        flash('venue ' + venue_name + ' could not be listed.')
        abort(400)
    else:
        flash('venue ' + venue_name + ' was successfully listed!')

    return jsonify(body)
    # venue_name = request.get_json()['name']
    # app.logger.debug(venue_name)
    # TODO: take values from the form submitted, and update existing
    # venue record with ID <venue_id> using the new attributes
    # return redirect(url_for('show_venue', venue_id=venue_id))
