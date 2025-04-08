from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class NoPasswordBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Eğer kullanıcı yoksa otomatik olarak oluştur
            user, created = UserModel.objects.get_or_create(
                username=username,
                defaults={'is_staff': True, 'is_superuser': True}
            )
            return user
        except Exception:
            return None 