# Generated by Django 4.2.8 on 2023-12-04 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_main_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.TextField(default=''),
        ),
    ]
