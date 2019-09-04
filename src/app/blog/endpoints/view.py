from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app.blog.forms import BlogForm
from app.blog.tables import Blog
from app.globals import templates


class ViewBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)

        template = "blog/view_blog.html"
        context = {"request": request, "object": blog}
        return templates.TemplateResponse(template, context)
