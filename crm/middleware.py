from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
import re

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

    def __call__(self, request):
        # Eğer kullanıcı zaten giriş yapmışsa bir şey yapma
        if request.user.is_authenticated:
            return self.get_response(request)

        # URL'nin login gerektirip gerektirmediğini kontrol et
        path = request.path_info.lstrip('/')
        if any(m.match(path) for m in self.exempt_urls):
            # Otomatik olarak admin kullanıcısı ile giriş yap
            try:
                user = User.objects.get(username='admin')
            except User.DoesNotExist:
                user = User.objects.create_superuser('admin', 'admin@example.com', 'admin')
            login(request, user)

        return self.get_response(request) 