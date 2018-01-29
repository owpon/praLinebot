"""empty message

Revision ID: 74786a4d99c1
Revises: 
Create Date: 2018-01-27 14:45:04.725705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74786a4d99c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('config',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('GroupId', sa.String(length=256), nullable=True),
    sa.Column('Item', sa.String(length=256), nullable=True),
    sa.Column('Status', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    op.create_table('words',
    sa.Column('Id', sa.Integer(), nullable=False),
    sa.Column('input_word', sa.String(length=256), nullable=True),
    sa.Column('output_word', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('Id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('words')
    op.drop_table('config')
    # ### end Alembic commands ###