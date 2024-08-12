def simple_middleware(get_request):
    def middleware(request):
        response = get_request(request)
        return response

    return middleware


class SimpleMiddleware:
    def __init__(self, get_request):  # Fixed typo: __inti__ to __init__
        self.get_request = get_request

    def __call__(self, request):
        response = self.get_request(request)  # Fixed typo: respose to response
        return response
