from django.db import models
from django.contrib.auth.models import User


class NewsPost(models.Model):
	headline = models.TextField()
	link = models.URLField()
	description = models.TextField(null=True)
	image_url = models.URLField(max_length=2000)
	publisher = models.CharField(max_length = 50)
	date_published = models.DateTimeField(null=True)
	category = models.CharField(max_length=20)

	def __str__(self):
		return f'{self.publisher} --- {self.category} --- {self.headline}'

class UserFeedList(models.Model):
	name = models.CharField(max_length=100)
	news_feeds = models.ManyToManyField('FeedLink', related_name='feeds')
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class FeedLink(models.Model):
	feed_url = models.URLField()
	category = models.CharField(max_length=30)

	def __str__(self):
		return self.feed_url


	

