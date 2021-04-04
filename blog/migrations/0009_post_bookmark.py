# Generated by Django 3.1.7 on 2021-04-03 20:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0008_auto_20210403_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='bookmark',
            field=models.ManyToManyField(related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
    ]