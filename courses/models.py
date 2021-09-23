from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Subject(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    #using this to order by title, it can be used to order by anything
    class Meta:
        ordering = ('title',) 

    def __str__(self):
        return self.title




class Course(models.Model):
    #owner : The instructor who created this course.
    owner = models.ForeignKey(User, related_name="courses_created", on_delete=models.CASCADE)#fk to User
    subject = models.ForeignKey(Subject, related_name="courses", on_delete=models.CASCADE)#fk to subject

    title = models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,unique=True)

    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.title

class Module(models.Model):
    
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE)#fk to Course

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title

