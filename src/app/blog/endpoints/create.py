from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app.blog.forms import BlogForm
from app.blog.tables import Blog
from app.globals import templates


class CreateBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        form = BlogForm()

        template = "blog/blog_form.html"
        context = {"request": request, "form": form}
        return templates.TemplateResponse(template, context)

    @requires("authenticated", redirect="auth:login")
    async def post(self, request):
        data = await request.form()
        form = BlogForm(data)

        if not form.validate():
            template = "blog/blog_form.html"
            context = {"request": request, "form": form}
            return templates.TemplateResponse(template, context)

        blog = Blog(
            title=form.title.data,
            meta_description=form.meta_description.data,
            author=form.author.data,
            post_body=form.post_body.data,
            is_live=form.is_live.data,
            created_by=request.user,
            last_updated_by=request.user,
        )

        blog.save()

        return RedirectResponse(url=request.url_for("blog:blog_admin"), status_code=302)
