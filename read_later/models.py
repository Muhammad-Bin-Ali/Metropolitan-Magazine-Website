from django.db import models
from django.contrib.auth.models import User
from main_news.models import NewsPost

class ReadLater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(NewsPost, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f'{self.user} --- {self.post.publisher}'