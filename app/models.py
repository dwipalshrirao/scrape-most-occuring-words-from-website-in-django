from django.db import models

# Create your models here.


class urls(models.Model):
    url=models.CharField(max_length=300)

    def __str__(self):
        return self.url


class top_words(models.Model):
    url=models.ForeignKey(urls,on_delete=models.CASCADE)
    word=models.CharField(max_length=100)
    frequency=models.PositiveIntegerField()