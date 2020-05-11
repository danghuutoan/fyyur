"""empty message

Revision ID: adbae09abc6e
Revises: 3b10edd9e9eb
Create Date: 2020-05-09 18:13:42.592555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adbae09abc6e'
down_revision = '3b10edd9e9eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    venue_genres = op.create_table('venue_genres',
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('venue_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], )
    )

    op.bulk_insert(
    venue_genres,
    [
        {'venue_id': 1, 'genre_id': 11},
        {'venue_id': 1, 'genre_id': 16},
        {'venue_id': 1, 'genre_id': 19},
        {'venue_id': 1, 'genre_id': 3},
        {'venue_id': 1, 'genre_id': 6},
        {'venue_id': 2, 'genre_id': 3},
        {'venue_id': 2, 'genre_id': 15},
        {'venue_id': 2, 'genre_id': 8},
        {'venue_id': 3, 'genre_id': 17},
        {'venue_id': 3, 'genre_id': 11},
        {'venue_id': 3, 'genre_id': 3},
        {'venue_id': 3, 'genre_id': 6},
    ])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_genres')
    # ### end Alembic commands ###