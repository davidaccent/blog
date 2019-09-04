def test_login_required(client):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grans_access(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"


def test_has_correct_context(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert "request" in response.context


# def test_invalid_post(client, login):


def test_post_create_user(client, login):
    url = client.app.url_path_for("blog:create_blog")

    # created_by_id=request.user.id, last_updated_by_id=request.user.id
    response = client.post(url, data={"title": "test", "author": "Ted"})

    # after saving page should be redirt to users screen
    assert response.status_code == 302
    assert response.next.url == f"http://testserver/blog/blog_admin"
