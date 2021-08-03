"""empty message

Revision ID: a2f66d84476e
Revises: fe518e11f5ff
Create Date: 2021-07-23 16:51:09.068732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2f66d84476e'
down_revision = 'fe518e11f5ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zhang_ting_list_table',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('rdatatime', sa.String(length=15), nullable=True),
    sa.Column('stockcode', sa.String(length=15), nullable=True),
    sa.Column('stockname', sa.String(length=25), nullable=True),
    sa.Column('jianjie', sa.String(length=500), nullable=True),
    sa.Column('bankuai', sa.String(length=50), nullable=True),
    sa.Column('shoubantime', sa.String(length=15), nullable=True),
    sa.Column('weibantime', sa.String(length=15), nullable=True),
    sa.Column('kaibancount', sa.Integer(), nullable=True),
    sa.Column('lianban', sa.Integer(), nullable=True),
    sa.Column('shizhi', sa.Integer(), nullable=True),
    sa.Column('huanshou', sa.Integer(), nullable=True),
    sa.Column('ztyuanyin', sa.String(length=1000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('zhang_ting_list_table')
    # ### end Alembic commands ###
