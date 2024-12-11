"""membuat tabel gambar

Revision ID: 745357ebf060
Revises: 2c4321816d87
Create Date: 2024-12-11 20:01:12.225476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '745357ebf060'
down_revision = '2c4321816d87'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('judul', sa.String(length=50), nullable=False),
    sa.Column('pathname', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gambar')
    # ### end Alembic commands ###
