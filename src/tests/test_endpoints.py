def test_login_not_required(client):
    url = client.app.url_path_for("home")
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/"


def test_login_grants_access(client, login):
    url = client.app.url_path_for("home")
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "home.html"


def test_has_correct_context(client, login):
    url = client.app.url_path_for("blog:blog_admin")
    response = client.get(url)

    assert "request" in response.context
