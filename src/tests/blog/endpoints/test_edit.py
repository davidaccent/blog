def test_login_required(client, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grants_access(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"


def test_has_correct_context(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.get(url)

    assert "request" in response.context


def test_post_edit_blog(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)

    response = client.post(
        url,
        data={
            "title": "title change",
            "author": "test",
            "meta_description": "test",
            "post_body": "test",
            "is_live": True,
        },
    )

    assert response.status_code == 302
    assert response.next.url == f"http://testserver/blog/blog_admin"


def test_form_invalid(client, login, blog):
    url = client.app.url_path_for("blog:edit_blog", blog_id=blog.id)
    response = client.post(url, data={"title": "", "author": "Ted"})

    assert response.status_code == 200
    assert response.template.name == "blog/blog_form.html"
    assert (
        response.url
        == f"http://testserver/blog/blog_admin/{blog.id}/view_blog/edit_blog"
    )
