from django.shortcuts import redirect


class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.path == '/login/' or request.path == '/register/':
            return response
        if not request.user.is_authenticated:
            return redirect('users:login_users')
        return response
