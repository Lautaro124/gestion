"""Fix

Revision ID: ffdac788a883
Revises: 33c96dceaa44
Create Date: 2023-06-21 21:54:20.223441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ffdac788a883'
down_revision = '33c96dceaa44'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_tipe_users_id', table_name='tipe_users')
    op.drop_table('tipe_users')
    op.drop_constraint('companys_users_id_fkey', 'companys', type_='foreignkey')
    op.drop_column('companys', 'users_id')
    op.drop_constraint('users_type_user_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'type_users', ['type_user_id'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_type_user_id_fkey', 'users', 'tipe_users', ['type_user_id'], ['id'], ondelete='SET NULL')
    op.add_column('companys', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('companys_users_id_fkey', 'companys', 'users', ['users_id'], ['id'], ondelete='SET NULL')
    op.create_table('tipe_users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='tipe_users_user_id_fkey', ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name='tipe_users_pkey'),
    sa.UniqueConstraint('name', name='tipe_users_name_key')
    )
    op.create_index('ix_tipe_users_id', 'tipe_users', ['id'], unique=False)
    # ### end Alembic commands ###