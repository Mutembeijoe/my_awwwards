# Generated by Django 2.2.7 on 2019-11-24 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_rating_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
