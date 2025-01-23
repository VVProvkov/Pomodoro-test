"""yandex-access-token

Revision ID: 3bf1e144213a
Revises: ee811113b4f0
Create Date: 2024-03-09 12:14:14.395475

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3bf1e144213a"
down_revision: Union[str, None] = "ee811113b4f0"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("UserProfile", sa.Column("yandex_access_token", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("UserProfile", "yandex_access_token")
    # ### end Alembic commands ###
