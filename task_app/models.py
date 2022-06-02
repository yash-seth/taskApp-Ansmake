from django.db import models

class Task(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=255, blank=False, default='')
    email = models.CharField(max_length=70, blank=False, default='')
    created_at = models.DateTimeField(auto_now_add=True)