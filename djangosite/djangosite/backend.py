from django.contrib.auth.backends import BaseBackend
from odoorpc import ODOO
from django.contrib.auth import get_user_model
User = get_user_model()

class MyBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        self.odoo_api = ODOO('web', port=8069)
        try:
            self.odoo_api.login('odoo13', username, password)
        except:
            return None
        self.uid = self.odoo_api.env.uid
        try:
            self.user_check = self.odoo_api.env.user
        except:
            self.user_check = None
        if self.user_check:
            group_indexes = self.odoo_api.env['res.groups'].search([('users.id','=',self.uid)])
            groups = self.odoo_api.env['res.groups'].browse(group_indexes)
            groups_str = str(groups._ids).replace(' ', '').strip('[]')
            s_tasks = self.odoo_api.env["project.task"].search([('user_id','=',self.uid)])
            tasks = self.odoo_api.env["project.task"].browse(s_tasks)
            tasks_str = str(tasks._ids).replace(' ', '').strip('[]')
            self.active = self.odoo_api.env.user.active
            if not self.active:
                #TODO: This may need to more action, but now, it's enough.
                return None
        if self.uid:
            try:
                user = User.objects.get(username=username)
                # update user.odoo_groups
                if self.user_check:
                    if user.odoo_groups != groups_str:
                        user.odoo_groups = groups_str
                        user.save()
                    if user.odoo_tasks != tasks_str:
                        user.odoo_tasks = tasks_str
                        user.save()
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = False
                user.is_superuser = False
                if self.user_check:
                    user.odoo_groups = groups_str
                    user.odoo_tasks = tasks_str
                user.save()
                # user.odoo_env = self.odoo_api.env
            return user
        return None
        
    def get_user(self, user_id):
        try:
            user = User.objects.get(pk=user_id)
            # user.odoo_env = self.odoo_api.env
            return user
        except User.DoesNotExist:
            return None


