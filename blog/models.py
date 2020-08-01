from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)

    pub_date=models.DateTimeField('date published')

    body=models.TextField()

    def __str__(self):
        return self.title

class QnA(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body=models.TextField()

    def __str__(self):
        return self.title

    def QnAsummary(self):
        return self.body[:100]

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def reviewSummary(self):
        return self.body[:100]
