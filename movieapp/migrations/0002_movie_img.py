# Generated by Django 4.0.6 on 2023-02-08 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default='dfddds', upload_to='pics'),
            preserve_default=False,
        ),
    ]
