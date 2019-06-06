from django.db import models

# Read more
# http://docs.djangoproject.com/en/2.2/ref/models/fields/

# Create your models here.
class Name(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Binding(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    binding = models.ForeignKey(Binding, on_delete=models.SET_NULL, null=True)
    year = models.PositiveSmallIntegerField()
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Transaction(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
        # return item.name + ": " + self.created