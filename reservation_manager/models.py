from django.db import models


class Base(models.Model):
    
    def __str__(self):
        return self.name