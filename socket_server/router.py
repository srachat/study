import http

from core import Request, Response
from views.index import index

URLS = {
    "/": index
}


def process_request(request: Request) -> Response:
    view = URLS.get(request.url)

    if not view:
        return Response(request, status_code=http.HTTPStatus.NOT_FOUND)

    content = view(request)
    return Response(request, status_code=http.HTTPStatus.OK, content=content, content_type="text/html")
