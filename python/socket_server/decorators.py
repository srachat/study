from functools import wraps
from typing import Callable, Sequence

from core import Request


def allow_methods(allowed_methods: Sequence[str]):
    """
    Adds a 'allowed_methods` property to a function object,
    which is than evaluated in the process_request function.

    Should be used as the following example:

        @allow_methods(['GET', 'POST'])
        def my_view(request):
            # I can assume now that only GET or POST requests make it this far
            # ...

    Now my_view.allowed_methods == ['GET', 'POST'].

    Note that request methods should be in uppercase.
    """
    def wrapper(function: Callable):
        function.allowed_methods = allowed_methods

        @wraps(function)
        def inner(request: Request, *args, **kwargs):
            return function(request, *args, **kwargs)
        return inner

    return wrapper
