from django.db import models


# Create your models here.
class Task(models.Model):
    PROJECTS = (
        ('Python', 'Python'),
        ('Django', 'Django'),
        ('Java', 'Java'),
        ('Android', 'Android'),
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    )

    name = models.CharField(max_length=200)
    projects = models.CharField(max_length=200, choices=PROJECTS)
    start = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    end = models.TimeField(auto_now_add=False, auto_now=False, blank=True)
    timestamp = models.TimeField(auto_now_add=True, auto_now=False, blank=True)
    status = models.CharField(max_length=200, choices=STATUS)

    def __str__(self):
        return self.name
