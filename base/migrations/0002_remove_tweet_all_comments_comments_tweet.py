# Generated by Django 4.1.4 on 2023-01-12 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='all_comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='tweet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tweet'),
        ),
    ]
