# Generated by Django 3.2.12 on 2022-03-06 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='intrest',
            field=models.TextField(default='python'),
            preserve_default=False,
        ),
    ]
