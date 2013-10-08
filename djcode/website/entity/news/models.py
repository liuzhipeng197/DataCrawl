from django.db import models

# Create your models here.
class KeyWord(models.Model):
	NkeyWord = models.CharField(max_length = 10)

class ContentUrl(models.Model):
	NUrl = models.CharField(max_length = 200)

class Info(models.Model):
	NewsTitle = models.CharField(max_length = 30)
	NewsDate = models.DateTimeField()
	NewsContent = models.TextField()
	NewsSource = models.CharField(max_length = 50)

