# Generated by Django 4.2.2 on 2023-07-15 07:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0006_alter_blog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 7, 15, 7, 25, 17, 653351, tzinfo=datetime.timezone.utc)),
        ),
    ]
