# Generated by Django 4.2.2 on 2023-06-28 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='content',
            field=models.CharField(max_length=1000),
        ),
    ]
