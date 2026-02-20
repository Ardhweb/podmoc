from django.contrib.auth.backends import ModelBackend
from accounts.models import User  
from django.db.models import Q
class CustomBackend(ModelBackend):
    def authenticate(self, request,username_or_email=None,password=None, **kwargs):
        try:
            user = User.objects.get(Q(email=username_or_email) | Q(username=username_or_email))
            if user.check_password(password):  # Check password manually
                return user
        except User.DoesNotExist:
            return None
        return None