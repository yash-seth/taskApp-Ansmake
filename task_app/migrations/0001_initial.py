# Generated by Django 4.0.4 on 2022-06-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=70)),
                ('email', models.CharField(default='', max_length=70)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
