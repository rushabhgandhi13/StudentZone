# Generated by Django 3.1.4 on 2021-04-03 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_prod_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='prod_img',
            field=models.ImageField(default='default_thumbnail.jpg', upload_to='Product_images'),
        ),
    ]
