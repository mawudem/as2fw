# Generated by Django 3.1.7 on 2021-02-27 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_projets_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='projets',
            name='author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]