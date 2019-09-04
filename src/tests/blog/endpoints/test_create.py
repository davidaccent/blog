def test_login_required(client):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


from app.blog.forms import BlogForm


def test_login_grants_access(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"


def test_has_correct_context(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.get(url)

    assert "request" in response.context


def test_post_create_blog(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.post(url, data={"title": "test", "author": "Ted"})

    assert response.status_code == 302
    assert response.next.url == f"http://testserver/blog/blog_admin"


def test_form_invalid(client, login):
    url = client.app.url_path_for("blog:create_blog")
    response = client.post(url, data={"title": "", "author": "Ted"})

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"
    assert response.url == f"http://testserver/blog/blog_admin/create_blog"
