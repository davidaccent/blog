from starlette.endpoints import HTTPEndpoint
from starlette.authentication import requires
from app.globals import templates


class Home(HTTPEndpoint):
    async def get(self, request):
        template = "home.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)

class Blog(HTTPEndpoint):
    @requires(["authenticated"])
    async def get(self, request):
        template = "blog_admin.html"
        context = {"request": request}
        return templates.TemplateResponse(template, context)
