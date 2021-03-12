from core import Request, Response, MethodNotAllowedResponse
from views.errors import not_found
from urls import urlpatterns


def process_request(request: Request) -> Response:
    view = urlpatterns.get(request.url)

    if not view:
        return not_found(request)

    allowed_methods = (list(getattr(view, "allowed_methods", [])) or ["GET"]) + ["HEAD"]
    if request.method not in allowed_methods:
        return MethodNotAllowedResponse(request, allowed_methods=allowed_methods)

    return view(request)
