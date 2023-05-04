"""init

Revision ID: 3e7b884808b7
Revises: 
Create Date: 2023-04-21 15:26:25.163368

"""
from sqlalchemy import create_engine

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from core.config import get_settings
from models.base import Base

revision = '3e7b884808b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # inside of a "create the database" script, first create
    # tables:
    engine = create_engine(get_settings().SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False},
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)


def downgrade() -> None:
    pass
