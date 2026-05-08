import jwt
from django.conf import settings
from django.shortcuts import redirect


class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        protected_urls = [
            '/dashboard',
            '/update',
            '/delete'
        ]

        if request.path in protected_urls:
            token = request.COOKIES.get('access_token')

            if not token:
                return redirect('/login')

            try:
                jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            except Exception:
                return redirect('/login')

        response = self.get_response(request)
        return response