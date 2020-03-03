# Generated by Django 3.0.3 on 2020-03-03 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('level', models.CharField(max_length=5)),
                ('zipcode', models.IntegerField(max_length=5)),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
            },
        ),
    ]
