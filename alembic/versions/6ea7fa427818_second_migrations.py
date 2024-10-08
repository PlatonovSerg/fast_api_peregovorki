"""Second migrations

Revision ID: 6ea7fa427818
Revises: 89b8a1a0810c
Create Date: 2024-09-12 11:11:45.669897

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6ea7fa427818'
down_revision: Union[str, None] = '89b8a1a0810c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('meetingroom', sa.Column('description', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('meetingroom', 'description')
    # ### end Alembic commands ###
