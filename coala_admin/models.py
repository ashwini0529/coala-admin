from __future__ import unicode_literals

from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=500)
	status = models.BooleanField(default=False) #If the blog is approved by a coala admin or not
	pub_date = models.DateTimeField('date published')
	description = models.TextField()
	views = models.IntegerField(default=0)
	feature_image_link = models.CharField(max_length=500) # feature image link of blog that could be used for og:image
	author = models.CharField(max_length=100)
class Tags(models.Model):
	tag = models.ForeignKey(Blog, on_delete=models.CASCADE)
