from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=20)
    slug = models.CharField(max_length=120)
    content = models.TextField()
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' - ' + self.author