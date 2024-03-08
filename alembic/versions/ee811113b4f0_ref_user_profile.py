"""ref-user-profile

Revision ID: ee811113b4f0
Revises: 1ff0f89372ac
Create Date: 2024-03-08 23:42:28.365527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ee811113b4f0'
down_revision: Union[str, None] = '1ff0f89372ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserProfile', 'username',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('UserProfile', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('UserProfile', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('UserProfile', 'username',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
