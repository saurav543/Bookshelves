# Generated by Django 3.1.1 on 2021-01-31 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updown', '0002_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
