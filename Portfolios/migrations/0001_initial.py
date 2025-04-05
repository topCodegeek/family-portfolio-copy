# Generated by Django 4.2.2 on 2023-06-22 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skillset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='Portfolios/Thumages')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
