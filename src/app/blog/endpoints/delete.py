from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app.blog.tables import Blog
from app.globals import templates


class DeleteBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)

        template = "blog/delete_blog.html"
        context = {"request": request, "object": blog}
        return templates.TemplateResponse(template, context)

    @requires("authenticated", redirect="auth:login")
    async def post(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)

        blog.delete()

        return RedirectResponse(url=request.url_for("blog:blog_admin"), status_code=302)
