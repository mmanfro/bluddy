from blood.models import User
from django.contrib.auth.backends import  ModelBackend
from blood.views import decrypt

class UserAuthBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        users = User.objects.all()
        for user in users:
            email = decrypt(email = user.email)['email']
            print(email)

            if email == username:
                return user
            else:
                pass