# Generated by Django 3.1.1 on 2021-01-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updown', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='file',
            field=models.FileField(default='', upload_to='media'),
            preserve_default=False,
        ),
    ]