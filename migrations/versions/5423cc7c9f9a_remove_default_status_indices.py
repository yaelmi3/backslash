"""Remove default status indices

Revision ID: 5423cc7c9f9a
Revises: 115fd26ea9a2
Create Date: 2017-05-14 16:22:36.680430

"""

# revision identifiers, used by Alembic.
revision = '5423cc7c9f9a'
down_revision = '115fd26ea9a2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_session_status', table_name='session')
    op.drop_index('ix_test_status', table_name='test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_test_status', 'test', ['status'], unique=False)
    op.create_index('ix_session_status', 'session', ['status'], unique=False)
    # ### end Alembic commands ###
