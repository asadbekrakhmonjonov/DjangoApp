from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=250, blank=False, null=False)
    address = models.CharField(max_length=250, blank=False, null=False)

    def __str__(self):
        return self.name
class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False, null=False)
    author = models.CharField(max_length=250, blank=False)
    genre = models.CharField(max_length=250, blank=False, null=False)
    condition = models.CharField(max_length=250, blank=False, null=False)
    def __str__(self):
        return self.title
