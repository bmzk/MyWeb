# Generated by Django 5.0.4 on 2024-04-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_zh', models.CharField(max_length=200)),
                ('name_en', models.CharField(max_length=200)),
                ('lvl', models.IntegerField(default=0)),
                ('input_time', models.DateTimeField(verbose_name='date input time')),
            ],
        ),
    ]
