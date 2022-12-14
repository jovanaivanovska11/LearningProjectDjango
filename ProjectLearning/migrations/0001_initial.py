# Generated by Django 4.0.4 on 2022-09-23 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time', models.IntegerField()),
                ('video', embed_video.fields.EmbedVideoField()),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=50)),
                ('answer', models.CharField(max_length=100, null=True)),
                ('quiz_lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectLearning.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='QuizForLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectLearning.lecture')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectLearning.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectLearning.lecture')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
