from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField

class Person(models.Model):
    class Course(models.TextChoices):
        Course1 = 'Programming for beginners'
        Course2 = 'Programming for programmers'
        Course3 = 'Programming for advanced programmers'
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    course = models.CharField(max_length=50,
                              choices=Course.choices,
                              default=Course.Course1, )
    def __str__(self):
        return self.name+" "+self.surname

class Lecture(models.Model):
    name = models.CharField(max_length=50)
    time = models.IntegerField()
    video = EmbedVideoField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Forum(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)

class Reply(models.Model):
    name = models.ForeignKey(Person, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)


