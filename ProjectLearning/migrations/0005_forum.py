# Generated by Django 4.0.4 on 2022-09-25 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectLearning', '0004_person_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
    ]
