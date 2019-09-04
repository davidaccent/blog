def test_login_required(client, blog):
    url = client.app.url_path_for("blog:delete_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grans_access(client, login, blog):
    url = client.app.url_path_for("blog:delete_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/delete_blog.html"


def test_invalid_id_404_error(client, login):
    url = client.app.url_path_for("blog:delete_blog", blog_id=9999)
    response = client.get(url)

    assert response.status_code == 404
