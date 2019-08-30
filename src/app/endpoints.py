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
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blogs = Blog.query.all()

        template = "blog_admin.html"
        context = {"request": request, "blogs": blogs}
        return templates.TemplateResponse(template, context)


class CreateBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        form = BlogForm()

        template = "create_blog.html"
        context = {"request": request, "form": form}
        return templates.TemplateResponse(template, context)

    @requires("authenticated", redirect="auth:login")
    async def post(self, request):
        data = await request.form()
        form = BlogForm(data)
        if not form.validate():
            template = "create_blog.html"
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
        return RedirectResponse(url=request.url_for("blog_admin"), status_code=302)


class ViewBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)
        
        template = "view_blog.html"
        context = {"request": request, "blog": blog}
        return templates.TemplateResponse(template, context)


class EditBlog(HTTPEndpoint):
    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)
        form = BlogForm(obj=blog)
        
        template = "edit_blog.html"
        context = {"request": request, "blog": blog, "form": form}
        return templates.TemplateResponse(template, context)

    @requires("authenticated", redirect="auth:login")
    async def get(self, request):
        blog_id = request.path_params["blog_id"]
        blog = Blog.query.get_or_404(blog_id)

        data = await request.form()
        form = BlogForm(data, obj=blog)

        if not form.validate():
            template = "edit_blog.html"
            context = {"request": request, "blog": blog, "form": form}
            return templates.TemplateResponse(template, context)

        blog.title = form.title.data
        blog.meta_description = form.meta_description.data
        blog.post_body = form.post_body.data
        blog.author = form.author.data
        blog.is_live = form.is_live.data

        blog.save()

        return RedirectResponse(url=request.url_for("view_blog"), status_code=302)
