from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=13)
    address = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class BlogModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    short_des = models.TextField(null=True)
    long_des = models.TextField(null=True)
    date = models.DateField(null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.title + " -- "+ self.cat.name

class LikeBlog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    blog = models.ForeignKey(BlogModel,on_delete=models.CASCADE,null=True)

class UserDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=100, null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.user.first_name