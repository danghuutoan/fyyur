"""empty message

Revision ID: c8ffe52845e4
Revises: e8585676dfba
Create Date: 2020-05-04 15:44:33.603560

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c8ffe52845e4'
down_revision = 'e8585676dfba'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('artist', 'genres')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('genres', postgresql.ARRAY(sa.VARCHAR(length=120)), autoincrement=False, nullable=True))
    # ### end Alembic commands ###