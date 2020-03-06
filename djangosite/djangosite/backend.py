from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from odoorpc import ODOO


class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        self.odoo_api = ODOO()
        self.odoo_api.login('odoo13', username, password)
        self.uid = self.odoo_api.env.uid
        if self.uid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None