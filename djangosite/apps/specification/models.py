from django.db import models

# Create your models here.
class Sepc(models.Model):
    name = models.CharField(max_length=10)

class SepcItem(models.Model):
    sepc = models.ForeignKey('Sepc',
                              on_delete=models.CASCADE,
                              related_name='item',
    )
    item = models.TextField()
