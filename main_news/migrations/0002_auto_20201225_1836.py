# Generated by Django 3.1.4 on 2020-12-25 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newspost',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='headline',
            field=models.TextField(),
        ),
    ]
