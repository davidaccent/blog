import sqlalchemy as sa
from starlette_core.testing import assert_model_field

from app.blog.tables import Blog


def test_fields():
    assert_model_field(Blog, "id", sa.Integer, False, True, True)
    assert_model_field(Blog, "created_by_id", sa.Integer, False, False, False)
    assert_model_field(Blog, "title", sa.String, False, False, True, 120)
    assert_model_field(Blog, "meta_description", sa.String, True, False, False, 120)
    assert_model_field(Blog, "author", sa.String, False, False, False, 120)
    assert_model_field(Blog, "post_body", sa.String, True, False, False)
    assert_model_field(Blog, "last_updated_by_id", sa.Integer, False, False, False)
    assert_model_field(Blog, "is_live", sa.Boolean, False, False, False)


def test_table_returns_id():
    assert str(Blog(id=1)) == "1"
