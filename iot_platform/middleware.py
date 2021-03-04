"""
Module Name: middleware
Descriptipn: Middleware is a framework of hooks into
             Django’s request/response processing.
             It’s a light, low-level “plugin” system for
             globally altering Django’s input or output.
"""


def open_access_middleware(get_response):
    def middleware(request):
        response = get_response(request)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    return middleware
