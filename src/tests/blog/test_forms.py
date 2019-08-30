from starlette_auth.tables import User
from starlette_core.testing import DummyPostData

from app.blog.forms import BlogForm


def test_valid():
    data = {
        "title": "Bundys Blog",
        "meta_description": "This is Bundys test blog",
        "author": "Ted Bundy",
        "post_body": "Article about something amazing",
        "is_live": False,
    }
    form = BlogForm(DummyPostData(data))
    assert form.validate()
    assert form.data == data


def test_valid_missing():
    data = {
        "title": "Bundys Blog",
        "meta_description": "",
        "author": "Ted Bundy",
        "post_body": "",
        "is_live": False,
    }
    form = BlogForm(DummyPostData(data))
    assert form.validate()
    assert form.data == data
