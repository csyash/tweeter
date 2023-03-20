# Generated by Django 4.1.4 on 2023-01-17 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_tweet_comments_comments_tweet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='tweet',
        ),
        migrations.AddField(
            model_name='tweet',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.comments'),
        ),
    ]
