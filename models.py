from django.db import models

# Create your models here.


class Create(models.Model):
    Title = models.CharField(max_length=300)
    Author = models.CharField(max_length=300)
    Comment = models.CharField(max_length=3000, blank=True)
    File = models.FileField(upload_to='documents/')
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title
