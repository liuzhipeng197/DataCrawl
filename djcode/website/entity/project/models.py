from django.db import models

# Create your models here.
class KeyWord(models.Model):
	PKeyWord = models.CharField(max_length = 10)
	PKeyClassified = models.CharField(max_length =20)

class ContentUrl(models.Model):
	PUrl = models.CharField(max_length = 200)

class Info(models.Model):
	ProjectTitle = models.CharField(max_length = 30)
	ProjectDate = models.CharField(max_length =20)
	ProjectContent = models.TextField()
	ProjectSource = models.CharField(max_length = 50)
	ProjectLogo = models.CharField(max_length =20)
	ProjectSort = models.CharField(max_length =20)

class Comment(models.Model):
	ProjectID = models.IntegerField()
	CommentDate = models.DateTimeField()
	CommentContent = models.TextField()
	CommentAuthor = models.CharField(max_length = 10)

