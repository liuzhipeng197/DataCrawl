from django.db import models

# Create your models here.
class KeyWord(models.Model):
	PKeyWord = models.CharField(max_length = 10)

class ContentUrl(models.Model):
	PUrl = models.CharField(max_length = 200)

class Info(models.Model):
	ProjectTitle = models.CharField(max_length = 30)
	ProjectDate = models.DateTimeField()
	ProjectContent = models.TextField()
	ProjectSource = models.CharField(max_length = 50)

class Comment(models.Model):
	ProjectID = models.IntegerField()
	CommentDate = models.DateTimeField()
	CommentContent = models.TextField()
	CommentAuthor = models.CharField(max_length = 10)

