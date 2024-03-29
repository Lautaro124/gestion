"""Check

Revision ID: 7b1a73399c39
Revises: 4ab15406a8ba
Create Date: 2023-06-29 23:53:38.986154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b1a73399c39'
down_revision = '4ab15406a8ba'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('type_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_type_users_id'), 'type_users', ['id'], unique=False)
    op.drop_index('ix_tipe_users_id', table_name='tipe_users')
    op.drop_table('tipe_users')
    op.drop_constraint('companys_description_key', 'companys', type_='unique')
    op.drop_constraint('companys_users_id_fkey', 'companys', type_='foreignkey')
    op.drop_column('companys', 'users_id')
    op.create_unique_constraint(None, 'users', ['type_user_id'])
    op.drop_constraint('users_type_user_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'type_users', ['type_user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_type_user_id_fkey', 'users', 'tipe_users', ['type_user_id'], ['id'], ondelete='SET NULL')
    op.drop_constraint(None, 'users', type_='unique')
    op.add_column('companys', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('companys_users_id_fkey', 'companys', 'users', ['users_id'], ['id'], ondelete='SET NULL')
    op.create_unique_constraint('companys_description_key', 'companys', ['description'])
    op.create_table('tipe_users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='tipe_users_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='tipe_users_pkey'),
    sa.UniqueConstraint('name', name='tipe_users_name_key')
    )
    op.create_index('ix_tipe_users_id', 'tipe_users', ['id'], unique=False)
    op.drop_index(op.f('ix_type_users_id'), table_name='type_users')
    op.drop_table('type_users')
    # ### end Alembic commands ###
