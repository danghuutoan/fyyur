"""empty message

Revision ID: 3b10edd9e9eb
Revises: 
Create Date: 2020-05-09 15:42:21.088736

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b10edd9e9eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    artist_table = op.create_table('artist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    genre_table = op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    venue_table = op.create_table('venue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    show_table = op.create_table('show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    artist_genres_table = op.create_table('artist_genres',
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('artist_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], )
    )
    # ### end Alembic commands ###

    op.bulk_insert(
    venue_table,
    [{
        "id": 1,
        "name": "The Musical Hop",
        "address": "1015 Folsom Street",
        "phone": "123-123-1234",
        "website": "https://www.themusicalhop.com",
        "facebook_link": "https://www.facebook.com/TheMusicalHop",
        "seeking_talent": True,
        "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
        "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
    },{
        "id": 2,
        "name": "The Dueling Pianos Bar",
        "address": "335 Delancey Street",
        "phone": "914-003-1132",
        "website": "https://www.theduelingpianos.com",
        "facebook_link": "https://www.facebook.com/theduelingpianos",
        "seeking_talent": False,
        "seeking_description": None,
        "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
    },{
        "id": 3,
        "name": "Park Square Live Music & Coffee",
        "address": "34 Whiskey Moore Ave",
        "phone": "415-000-1234",
        "website": "https://www.parksquarelivemusicandcoffee.com",
        "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
        "seeking_talent": False,
        "seeking_description": None,
        "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
    }])

    op.bulk_insert(
    artist_table,
    [{
        "id": 1,
        "name": "Guns N Petals",
        "phone": "326-123-5000",
        "website": "https://www.gunsnpetalsband.com",
        "facebook_link": "https://www.facebook.com/GunsNPetals",
        "seeking_venue": True,
        "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
        "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
        },{
        "id": 2,
        "name": "Matt Quevedo",
        "phone": "300-400-5000",
        "facebook_link": "https://www.facebook.com/mattquevedo923251523",
        "website": None,
        "seeking_venue": False,
        "seeking_description": None,
        "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
        },{
        "id": 3,
        "name": "The Wild Sax Band",
        "phone": "432-325-5432",
        "seeking_venue": False,
        "seeking_description": None,
        "website": None,
        "facebook_link": None,
        "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
        }])

    op.bulk_insert(
    genre_table,
    [
    {'id': 1, 'name': 'Alternative'},
    {'id': 2, 'name': 'Blues'},
    {'id': 3, 'name': 'Classical'},
    {'id': 4, 'name': 'Country'},
    {'id': 5, 'name': 'Electronic'},
    {'id': 6, 'name': 'Folk'},
    {'id': 7, 'name': 'Funk'},
    {'id': 8, 'name': 'Hip-Hop'},
    {'id': 9, 'name': 'Heavy Metal'},
    {'id': 10, 'name': 'Instrumental'},
    {'id': 11, 'name': 'Jazz'},
    {'id': 12, 'name': 'Musical Theatre'},
    {'id': 13, 'name': 'Pop'},
    {'id': 14, 'name': 'Punk'},
    {'id': 15, 'name': 'R&B'},
    {'id': 16, 'name': 'Reggae'},
    {'id': 17, 'name': 'Rock n Roll'},
    {'id': 18, 'name': 'Soul'},
    {'id': 19, 'name': 'Swing'},
    {'id': 20, 'name': 'Other'}])

    op.bulk_insert(
    artist_genres_table,
    [
        {'artist_id': 1, 'genre_id': 17},
        {'artist_id': 2, 'genre_id': 11},
        {'artist_id': 3, 'genre_id': 11},
        {'artist_id': 1, 'genre_id': 3}
    ])
def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_genres')
    op.drop_table('show')
    op.drop_table('venue')
    op.drop_table('genre')
    op.drop_table('artist')
    # ### end Alembic commands ###