from django.db import models
from django.db.models import CASCADE

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cars(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='Cars/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(models.Model):
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    contactemail = models.CharField(max_length=100)


    def __str__(self):
        return self.name




