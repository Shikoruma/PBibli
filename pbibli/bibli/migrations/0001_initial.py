# Generated by Django 2.2.7 on 2019-12-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20)),
                ('serie_title', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('num_volume', models.IntegerField()),
                ('author', models.CharField(max_length=30)),
                ('localisation', models.CharField(max_length=20)),
                ('demat', models.BooleanField()),
                ('abstract', models.CharField(max_length=200)),
            ],
        ),
    ]
