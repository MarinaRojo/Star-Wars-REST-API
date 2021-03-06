"""empty message

Revision ID: 67154473da7e
Revises: 15791a4b1d49
Create Date: 2022-02-12 10:33:45.331837

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67154473da7e'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('diameter', sa.Integer(), nullable=False),
    sa.Column('rotation_period', sa.Integer(), nullable=False),
    sa.Column('orbital_period', sa.Integer(), nullable=False),
    sa.Column('gravity', sa.String(length=80), nullable=False),
    sa.Column('population', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=20), nullable=False),
    sa.Column('terrain', sa.String(length=20), nullable=False),
    sa.Column('surface_water', sa.Integer(), nullable=False),
    sa.Column('created', sa.String(length=50), nullable=False),
    sa.Column('edited', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('character',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Integer(), nullable=False),
    sa.Column('hair_color', sa.String(length=20), nullable=False),
    sa.Column('skin_color', sa.String(length=20), nullable=False),
    sa.Column('eye_color', sa.String(length=20), nullable=False),
    sa.Column('birth_year', sa.String(length=20), nullable=False),
    sa.Column('gender', sa.String(length=20), nullable=False),
    sa.Column('created', sa.String(length=50), nullable=False),
    sa.Column('edited', sa.String(length=50), nullable=False),
    sa.Column('homeworld', sa.String(length=50), nullable=False),
    sa.Column('url', sa.String(length=250), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['character.id'], ),
    sa.ForeignKeyConstraint(['planet_id'], ['planet.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('name', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'name')
    op.drop_table('favorite')
    op.drop_table('character')
    op.drop_table('planet')
    # ### end Alembic commands ###
