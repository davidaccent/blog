from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app import db
from app.blog.forms import BlogForm
from app.blog.tables import Blog
from app.globals import templates


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)


class BlogAdmin(HTTPEndpoint):
    @requires(["authenticated"])
    async def get(self, request):
        template = "blog_admin.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)


class CreateBlog(HTTPEndpoint):
    @requires(["authenticated"])
    async def get(self, request):
        form = BlogForm()

        template = "create_blog.html"
        context = {"request": request, "form": form}
        return templates.TemplateResponse(template, context)


    async def post(self, request):

        data = await request.form()
        form = BlogForm(data)

        if not form.validate():
            template = "create_blog.html"
            context = {"request": request, "form": form}
            return templates.TemplateResponse(template, context)

        blog = Blog
        blog.title = form.title.data
        blog.meta_description = form.meta_description.data
        blog.author = form.author.data
        blog.post_body = form.post_body.data

        blog.save()

        return RedirectResponse(url=request.url_for("blog_admin"), status_code=302)