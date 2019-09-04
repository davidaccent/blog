def test_login_required(client, blog):
    url = client.app.url_path_for("blog:view_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grans_access(client, login, blog):
    url = client.app.url_path_for("blog:view_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/view_blog.html"


# def test_has_correct_context(client, login):
#     url = client.app.url_path_for("blog:view_blog")
#     response = client.get(url)

#     assert "request" in response.context
