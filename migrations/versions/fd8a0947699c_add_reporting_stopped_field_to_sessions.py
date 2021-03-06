"""Add reporting_stopped field to sessions

Revision ID: fd8a0947699c
Revises: 8f864a7768f8
Create Date: 2019-03-25 10:36:21.820432

"""

# revision identifiers, used by Alembic.
revision = 'fd8a0947699c'
down_revision = '8f864a7768f8'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('session', sa.Column('reporting_stopped', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('session', 'reporting_stopped')
    # ### end Alembic commands ###
