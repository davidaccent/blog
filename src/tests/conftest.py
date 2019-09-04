import pytest
from sqlalchemy_utils import create_database, database_exists, drop_database
from starlette.config import environ
from starlette.testclient import TestClient

environ["TESTING"] = "TRUE"

from app import db, main, settings  # noqa isort:skip
from starlette_core.database import Session  # noqa isort:skip


@pytest.fixture(scope="session", autouse=True)
def database():
    url = str(settings.DATABASE_URL)
    dbase = db.db

    if database_exists(url):
        drop_database(url)

    create_database(url)

    dbase.drop_all()
    dbase.create_all()

    return dbase


@pytest.fixture
def user():
    from starlette_auth.tables import User  # noqa isort:skip

    data = {"email": "test@example.com", "first_name": "Test", "last_name": "User"}

    try:
        return User.query.filter(email == data["email"]).one()
    except:
        usr = User(**data)
        usr.set_password("password")
        usr.save()
        return usr


@pytest.yield_fixture(scope="function", autouse=False)
def client():
    with TestClient(main.app) as client:
        yield client


@pytest.yield_fixture(scope="function", autouse=True)
def session(database):
    sess = Session()
    yield sess
    database.truncate_all()


@pytest.fixture
def login(client, user):
    client.post("/auth/login", data={"email": user.email, "password": "password"})


@pytest.fixture
def blog(user):
    from app.blog.tables import Blog

    object = Blog(
        title="test", author="Ted", created_by_id=user.id, last_updated_by_id=user.id
    )
    object.save()

    return object
