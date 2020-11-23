from core import Request, Response
from views.errors import not_found
from urls import urlpatterns


def process_request(request: Request) -> Response:
    view = urlpatterns.get(request.url)

    if not view:
        return not_found(request)

    return view(request)
