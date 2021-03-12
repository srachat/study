from core import Request, TemplateResponse
from template_render import render_template


def index(request: Request):
    content = render_template("index.html", data={"agent": request.headers.get("User-Agent")})
    return TemplateResponse(request, content=content)
