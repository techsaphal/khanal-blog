# Generated by Django 3.0.2 on 2021-07-25 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="khanal's blog", max_length=255),
        ),
    ]