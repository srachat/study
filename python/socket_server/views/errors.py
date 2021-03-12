from core import Request, TemplateResponse
from template_render import render_template


def not_found(request: Request):
    content = render_template("not_found.html", data={"url": request.url})
    return TemplateResponse(request, content=content)
