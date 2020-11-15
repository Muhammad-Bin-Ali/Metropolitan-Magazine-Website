from huey import crontab
from huey.contrib.djhuey import db_periodic_task
from .models import NewsPost
from .parse_function import parseRSSfeeds
import datetime
import pytz

@db_periodic_task(crontab(minute='*/1'))
def get_and_save_news():
	news_items = parseRSSfeeds()
	for item in news_items:
		post = NewsPost(
			headline = item['headline'], 
			link = item['link'], 
			image_url = item['image_url'],
			publisher = item['publisher'],
			date_published = item['date'],
			description = item['description'],
			category = item['category']
			)
		if NewsPost.objects.filter(headline = item['headline']):
			continue
		post.save()

@db_periodic_task(crontab(hour='*/1'))
def remove_old_stories():
	current_time_utc = pytz.utc.localize(datetime.datetime.utcnow())	
	top_posts = NewsPost.objects.filter(category = 'Top Stories',
										 date_published__lte = current_time_utc - datetime.timedelta(days=1))
	for post in top_posts:
		post.category = 'Old Top Stories'
		post.save()