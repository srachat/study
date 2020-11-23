import os
import socketserver
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core import Request
from router import process_request


class SimpleTCPHandler(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print(f"Address: {self.client_address}")

        data = self.request.recv(1024).strip()
        request = Request(data)
        response = process_request(request)

        self.request.send(response.prepare())


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with ThreadingTCPServer(("", 8888), SimpleTCPHandler) as server:
        print("Server started!")
        server.serve_forever()
