# Generated by Django 4.0.4 on 2022-09-29 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectLearning', '0008_reply'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quizforlecture',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='quizforlecture',
            name='quiz',
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
        migrations.DeleteModel(
            name='QuizForLecture',
        ),
    ]