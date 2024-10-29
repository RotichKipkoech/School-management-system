"""Add user_id to PasswordResetRequest

Revision ID: a049d67db46f
Revises: 93d76ffe8f60
Create Date: 2024-10-29 17:16:50.395802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a049d67db46f'
down_revision = '93d76ffe8f60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('password_reset_request', schema=None) as batch_op:
        batch_op.alter_column('reason',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('password_reset_request', schema=None) as batch_op:
        batch_op.alter_column('reason',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###