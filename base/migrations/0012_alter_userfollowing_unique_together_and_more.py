# Generated by Django 4.1.4 on 2023-01-26 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_rename_user_id_userfollowing_user_who_is_following_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together={('user_who_is_following', 'user_who_is_getting_followed')},
        ),
        migrations.AddConstraint(
            model_name='userfollowing',
            constraint=models.UniqueConstraint(fields=('user_who_is_following', 'user_who_is_getting_followed'), name='unique_followers'),
        ),
    ]
