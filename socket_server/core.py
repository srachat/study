import json
from typing import Iterator, Optional, Dict, Union
import http


class ContentType:
    APPLICATION_JSON = "application/json"


class RequestError(Exception):
    def __init__(self, status: int, status_message: Optional[str] = None):
        self.status = status
        self.status_message = status_message


class Request:
    def __init__(self, data: bytes):
        self.headers = {}
        self.data = None
        self.method = None
        self.url = None
        self.version = None

        self._parse_data(data)

    def _parse_data(self, data: bytes):
        split_data = iter(data.decode().split("\r\n"))

        try:
            self._parse_request_line(split_data)
            self._parse_headers(split_data)
            self._parse_request_data(split_data)
        except StopIteration:
            pass

    def _parse_request_line(self, unprocessed_line: Iterator[str]):
        split_line = next(unprocessed_line).split(" ")

        if len(split_line) != 3:
            raise RequestError(http.HTTPStatus.BAD_REQUEST, "Incorrect request line")

        self.method, self.url, self.version = split_line

    def _parse_headers(self, split_data: Iterator[str]):
        header = next(split_data)

        while header != "":
            header = header.split(":")
            self.headers[header[0]] = header[1].strip()
            header = next(split_data)

    def _parse_request_data(self, split_data: Iterator[str]):
        data = next(split_data)

        if self.headers.get("Content-Type") == ContentType.APPLICATION_JSON:
            self.data = json.loads(data)


class Response:
    content_type = None

    def __init__(
            self,
            request: Request,
            *,
            status_code: Union[http.HTTPStatus, int] = http.HTTPStatus.OK,
            headers: Optional[Dict[str, str]] = None,
            content: Optional[str] = None,
            content_type: Optional[str] = None
    ):
        self.request = request
        self.status_code = Response._parse_status_code(status_code)  # type: http.HTTPStatus
        self.content = content
        self.content_type = content_type or self.content_type or "text/plain"
        self.headers = self._prepare_headers(headers)

    @staticmethod
    def _parse_status_code(status_code: Union[http.HTTPStatus, int]):
        if isinstance(status_code, int):
            return http.HTTPStatus(status_code)
        else:
            return status_code

    def _prepare_headers(self, headers: Optional[Dict[str, str]]):
        headers = headers or {}

        required_headers = {
            "Server": "Cool server",
            "Connection": self.request.headers.get("Connection", "keep-alive")
        }
        if self.content:
            required_headers["Content-Type"] = self.content_type
            required_headers["Content-Length"] = len(self.content)

        headers.update(required_headers)

        return headers

    def prepare(self):
        status_line = f"{self.request.version} {self.status_code.value} {self.status_code.phrase}\r\n"

        headers = "\r\n".join(f"{name}: {value}" for name, value in self.headers.items()) + "\r\n"

        result = status_line + headers + "\r\n"

        if self.content:
            result += self.content

        return result.encode()


class TemplateResponse(Response):
    content_type = "text/html"


class JSONResponse(Response):
    content_type = "application/json"
