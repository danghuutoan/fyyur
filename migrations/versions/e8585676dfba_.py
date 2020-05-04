"""empty message

Revision ID: e8585676dfba
Revises: 83907b7f5e1a
Create Date: 2020-05-04 15:09:13.126004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8585676dfba'
down_revision = '83907b7f5e1a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genre', sa.Column('name', sa.String(), nullable=True))
    op.drop_column('genre', 'naem')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('genre', sa.Column('naem', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('genre', 'name')
    # ### end Alembic commands ###
