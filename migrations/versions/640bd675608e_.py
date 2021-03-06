"""empty message

Revision ID: 640bd675608e
Revises: b75c7e34f8ca
Create Date: 2020-05-13 11:21:47.135510

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '640bd675608e'
down_revision = 'b75c7e34f8ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    city_table = op.create_table('city',
                                 sa.Column('id', sa.Integer(), nullable=False),
                                 sa.Column('name', sa.String(
                                     length=120), nullable=True),
                                 sa.PrimaryKeyConstraint('id')
                                 )
    op.drop_table('venue_state')
    op.add_column('venue', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'venue', 'city', ['city_id'], ['id'])
    op.drop_column('venue', 'city')
    # ### end Alembic commands ###
    op.bulk_insert(
        city_table,
        [
            {"id": 1, 'name': "San Francisco"},
            {"id": 2, 'name': "New York"},
        ])

    op.execute('UPDATE venue SET city_id=1 WHERE id = 1')
    op.execute('UPDATE venue SET city_id=1 WHERE id = 3')
    op.execute('UPDATE venue SET city_id=2 WHERE id = 2')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('city', sa.VARCHAR(
        length=120), autoincrement=False, nullable=True))
    # op.drop_constraint(None, 'venue', type_='foreignkey')
    op.drop_column('venue', 'city_id')
    op.create_table('venue_state',
                    sa.Column('venue_id', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.Column('state_id', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.ForeignKeyConstraint(
                        ['state_id'], ['state.id'], name='venue_state_state_id_fkey'),
                    sa.ForeignKeyConstraint(
                        ['venue_id'], ['venue.id'], name='venue_state_venue_id_fkey')
                    )
    op.drop_table('city')
    # ### end Alembic commands ###
