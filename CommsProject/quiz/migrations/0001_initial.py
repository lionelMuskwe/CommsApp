# Generated by Django 4.0 on 2021-12-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('q1Question', models.CharField(max_length=100)),
                ('q1Answer', models.CharField(max_length=100)),
                ('q1FakeAnswers', models.CharField(max_length=100)),
                ('q2Question', models.CharField(max_length=100)),
                ('q2Answer', models.CharField(max_length=100)),
                ('q2FakeAnswers', models.CharField(max_length=100)),
            ],
        ),
    ]
