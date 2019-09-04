def test_login_required(client):
    url = client.app.url_path_for("blog:blog_admin")
    response = client.get(url)

    assert response.status_code == 200
    assert response.url == "http://testserver/auth/login"


def test_login_grans_access(client, login):
    url = client.app.url_path_for("blog:blog_admin")
    response = client.get(url)

    assert response.status_code == 200
    assert response.template.name == "blog/blog_admin.html"


def test_has_correct_context(client, login):
    url = client.app.url_path_for("blog:blog_admin")
    response = client.get(url)

    assert "request" in response.context


def test_table_generation(client, login):
    url = client.app.url_path_for("blog:blog_admin")
    # blog_data = blog
    response = client.get(url)
    assert "<th>Title</th>" in response.text
    assert "<th>Author</th>" in response.text
    assert "<th>Created By</th>" in response.text
    assert "<th>Date Created</th>" in response.text
    assert "<th>Status</th>" in response.text
    assert "<th>Update</th>" in response.text

    # assert blog_data.title in response
    # assert blog_data.author in response
    # assert blog_data.created_by in response
    # assert blog_data.created in response
    # if blog_data.is_active == False:
    #     assert "Inactive" in response.text
    # else:
    #     assert "Active" in response.text
