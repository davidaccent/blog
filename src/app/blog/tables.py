import sqlalchemy as sa
from sqlalchemy import PrimaryKeyConstraint, orm
from sqlalchemy_utils import Timestamp
from starlette_auth.tables import User
from starlette_core.database import Base


class Blog(Base, Timestamp):
    id = sa.Column(
        sa.Integer, nullable=False, primary_key=True, index=True, unique=True
    )
    created_by_id = sa.Column(sa.Integer, sa.ForeignKey(User.id), nullable=False)
    title = sa.Column(sa.String(120), nullable=False, unique=True)
    meta_description = sa.Column(sa.String(120))
    author = sa.Column(sa.String(120), nullable=False)
    post_body = sa.Column(sa.Text())
    last_updated_by_id = sa.Column(sa.Integer, sa.ForeignKey(User.id), nullable=False)
    is_live = sa.Column(sa.Boolean, nullable=False, default=False)

    created_by = orm.relationship("User", foreign_keys=[created_by_id])
    last_updated_by = orm.relationship("User", foreign_keys=[last_updated_by_id])
