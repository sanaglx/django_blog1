from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#class MyManager(models.Manager):
#    use_in_migrations = True

#class MyModel(models.Model):
#    objects = MyManager()

SHORT_TEXE_LEN=200

class Article(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXE_LEN:
            return self.text[:SHORT_TEXE_LEN]
        else:
            return self.text

class TableX(models.Model):
    name = models.CharField(max_length=100)
    fam = models.CharField(max_length=100)
    user = models.ForeignKey(User)










