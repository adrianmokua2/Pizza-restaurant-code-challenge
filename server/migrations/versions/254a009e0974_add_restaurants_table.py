"""Add restaurants table

Revision ID: 254a009e0974
Revises: 
Create Date: 2024-01-22 10:54:51.766667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '254a009e0974'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('address', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('restaurants')
    # ### end Alembic commands ###