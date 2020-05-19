"""empty message

Revision ID: d6c60d37b549
Revises: 837706595e1b
Create Date: 2020-05-14 16:26:38.454118

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6c60d37b549'
down_revision = '837706595e1b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('city_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'artist', 'city', ['city_id'], ['id'])
    op.drop_column('artist', 'city')
    # ### end Alembic commands ###
    op.execute('UPDATE artist SET city_id=1 WHERE id = 1')
    op.execute('UPDATE artist SET city_id=2 WHERE id = 2')
    op.execute('UPDATE artist SET city_id=1 WHERE id = 3')


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('city', sa.VARCHAR(
        length=120), autoincrement=False, nullable=True))
    # op.drop_constraint(None, 'artist', type_='foreignkey')
    op.drop_column('artist', 'city_id')
    # ### end Alembic commands ###
