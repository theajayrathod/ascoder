from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 13)
    email = models.CharField(max_length = 100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return ' Message from '  + self.name  + '-' + self.email


class AddQuestion(models.Model):
    sno = models.AutoField(primary_key = True)
    title = models.TextField(null = True, blank = True)
    status = models.CharField(default = 'inactive', max_length = 10)
    created_by = models.ForeignKey(User, null = True, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add = True )
    updated_at = models.DateField(auto_now = True)
    
    def __str__(self):
        return self.title

class Addanswer(models.Model):
    sno = models.AutoField(primary_key = True)
    ques_id = models.IntegerField(default=True)
    img_ans = models.ImageField(null = True, blank = True)
    answer = models.TextField()
    author = models.CharField(max_length = 13)
    slug = models.CharField(max_length = 130)


    def __str__(self):
        return  self.author


class CreatePost(models.Model):
    sno = models.AutoField(primary_key = True)
    question = models.CharField(max_length = 255)
    answer = models.TextField()
    author = models.CharField(max_length = 13)


    def __str__(self):
        return  self.author

    
