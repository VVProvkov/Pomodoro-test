"""access_token

Revision ID: b863de82ee3f
Revises: ff902b08f508
Create Date: 2024-03-08 17:10:03.148757

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b863de82ee3f"
down_revision: Union[str, None] = "ff902b08f508"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("UserProfile", "access_token")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("UserProfile", sa.Column("access_token", sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
