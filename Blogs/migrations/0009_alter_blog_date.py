# Generated by Django 4.2.2 on 2024-02-06 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0008_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 2, 6, 4, 0, 4, 152909, tzinfo=datetime.timezone.utc)),
        ),
    ]
