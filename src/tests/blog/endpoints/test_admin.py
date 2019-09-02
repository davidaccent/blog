from starlette.testclient import TestClient
from starlette_auth.tables import User

from app.main import app

url = app.url_path_for("blog:blog_admin")
login_data = {"email": "ted@example.com", "password": "password"}


def test_login_required():
    with TestClient(app) as client:
        response = client.get(url)

        assert response.status_code == 200
        assert response.url == "http://testserver/auth/login"


def test_logged_in_grants_access():
    with TestClient(app) as client:
        client.post("/auth/login", data=login_data)
        response = client.get(url)

        assert response.status_code == 200
        assert response.url == "http://testserver/blog/blog_admin"
        assert "request" in response.context
        assert response.template.name == "blog_admin.html"
