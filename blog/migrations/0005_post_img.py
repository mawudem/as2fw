# Generated by Django 3.1.7 on 2021-02-26 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
