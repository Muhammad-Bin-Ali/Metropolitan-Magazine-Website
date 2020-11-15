# Generated by Django 3.1 on 2020-11-02 02:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_news', '0004_auto_20201004_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_url', models.URLField()),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserFeedList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('news_feeds', models.ManyToManyField(related_name='feeds', to='main_news.FeedLink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
