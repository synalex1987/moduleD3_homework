# Generated by Django 4.1.1 on 2022-09-28 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('ART', 'Article'), ('NS', 'News')], default='NS', max_length=3),
        ),
    ]
