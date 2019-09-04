from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app.blog.forms import BlogForm
from app.blog.tables import Blog
from app.globals import templates


class BlogAdmin(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blogs = Blog.query.all()

        template = "blog/blog_admin.html"
        context = {"request": request, "object": blogs}

        return templates.TemplateResponse(template, context)
