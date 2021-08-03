"""empty message

Revision ID: fe518e11f5ff
Revises: 8c1b2b349a76
Create Date: 2021-07-23 08:47:33.091492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe518e11f5ff'
down_revision = '8c1b2b349a76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dat_list_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rdatatime', sa.String(length=15), nullable=True),
    sa.Column('yzname', sa.String(length=255), nullable=True),
    sa.Column('stockcode', sa.String(length=15), nullable=True),
    sa.Column('stockname', sa.String(length=25), nullable=True),
    sa.Column('buy', sa.Integer(), nullable=True),
    sa.Column('sell', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dat_list_table')
    # ### end Alembic commands ###
