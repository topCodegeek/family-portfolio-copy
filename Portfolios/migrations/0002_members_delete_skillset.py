# Generated by Django 4.2.2 on 2023-06-24 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(upload_to='Portfolios/Thumages')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Skillset',
        ),
    ]
