"""Added Mark Table.

Revision ID: 9436923fba42
Revises: 7bbf6f689122
Create Date: 2024-10-29 12:36:12.274279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9436923fba42'
down_revision = '7bbf6f689122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.Column('subject', sa.String(length=100), nullable=False),
    sa.Column('score', sa.Float(), nullable=False),
    sa.Column('test_type', sa.String(length=20), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teacher.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mark')
    # ### end Alembic commands ###
