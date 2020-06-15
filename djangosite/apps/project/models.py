from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    'odoo_groups is a string of number and created and updated in authenticate of MyBackend.'
    odoo_groups = models.CharField(default='', max_length=300, blank=True)
    odoo_tasks = models.CharField(default='', max_length=300, blank=True)

class Task(models.Model):
    '目前一個專案就是一台機器，我們會在name上加上專案的編號'
    # company = models.ForeignKey('Company', 
    #                             on_delete=models.CASCADE,
    #                             related_name='project',
    # )
    project_id = models.IntegerField(_("Project id"), blank=True)
    task_id = models.CharField(_("Task id."), max_length=10, blank=True)
    email_from = models.CharField(_("E-mail"), max_length=30)
    name = models.CharField(_("Name"), max_length=30)
    code = models.CharField(_("Code"), max_length=10, blank=True)
    manufacturer = models.CharField(_("manufacturer"), max_length=30, blank=True)
    # data_of_manufacture = models.DateField(blank=True)

    def __str__(self):
        return self.name
