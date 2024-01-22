"""Update restaurant_ pizzas and restaurant tables

Revision ID: 971b3f69263a
Revises: 4f06a6d72d38
Create Date: 2024-01-22 10:58:41.385273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '971b3f69263a'
down_revision = '4f06a6d72d38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pizza_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key('fk_pizza_id', 'pizzas', ['pizza_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.drop_constraint('fk_pizza_id', type_='foreignkey')
        batch_op.drop_column('pizza_id')

    # ### end Alembic commands ###