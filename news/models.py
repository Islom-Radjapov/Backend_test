from django.db import models

# Create your models here.

class Add_news(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title