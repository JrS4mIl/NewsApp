# Generated by Django 4.2.8 on 2023-12-09 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_created_date_news_update_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='ocatid',
            field=models.IntegerField(default=0),
        ),
    ]
