"""company

Revision ID: 5780f39ab661
Revises: d2dc3d4089f1
Create Date: 2023-07-05 21:06:47.231876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5780f39ab661'
down_revision = 'd2dc3d4089f1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    ## Delete company relation to user table
    op.drop_constraint('fk_company_user', 'users', type_='foreignkey')
    op.drop_column('users', 'company_id')
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
