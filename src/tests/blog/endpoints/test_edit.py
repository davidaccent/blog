def test_login_required(client, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grans_access(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"


def test_has_correct_context(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert "request" in response.context
