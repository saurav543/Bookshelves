# Generated by Django 3.1.1 on 2021-01-31 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('picture', models.ImageField(upload_to='')),
                ('auther', models.CharField(default='anonymous', max_length=30)),
                ('discribe', models.TextField(default='django uploaded file')),
            ],
        ),
    ]
