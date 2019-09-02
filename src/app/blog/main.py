from starlette.routing import Route, Router

from . import endpoints

app = Router(
    [
        Route(
            "/blog_admin",
            endpoint=endpoints.BlogAdmin,
            methods=["GET"],
            name="blog_admin",
        ),
        Route(
            "/blog_admin/create_blog",
            endpoint=endpoints.CreateBlog,
            methods=["GET", "POST"],
            name="create_blog",
        ),
        Route(
            "/blog_admin/{blog_id:int}/view_blog",
            endpoints.ViewBlog,
            methods=["GET"],
            name="view_blog",
        ),
        Route(
            "/blog_admin/{blog_id:int}/view_blog/edit_blog",
            endpoints.EditBlog,
            methods=["GET", "POST"],
            name="edit_blog",
        ),
    ]
)
