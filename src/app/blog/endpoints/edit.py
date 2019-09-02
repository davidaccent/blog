from starlette.authentication import requires
from starlette.endpoints import HTTPEndpoint
from starlette.responses import RedirectResponse

from app.blog.forms import BlogForm
from app.blog.tables import Blog
from app.globals import templates


class EditBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)
        form = BlogForm(obj=blog)

        template = "blog/edit_blog.html"
        context = {"request": request, "blog": blog, "form": form}
        return templates.TemplateResponse(template, context)

    @requires("authenticated", redirect="auth:login")
    async def post(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)

        data = await request.form()
        form = BlogForm(data, obj=blog)

        if not form.validate():
            template = "blog/edit_blog.html"
            context = {"request": request, "blog": blog, "form": form}
            return templates.TemplateResponse(template, context)

        blog.title = form.title.data
        blog.meta_description = form.meta_description.data
        blog.post_body = form.post_body.data
        blog.author = form.author.data
        blog.is_live = form.is_live.data

        blog.save()

        return RedirectResponse(url=request.url_for("view_blog"), status_code=302)
