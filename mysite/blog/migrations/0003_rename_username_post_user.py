# Generated by Django 4.2.9 on 2024-02-01 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_username_comment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='user',
        ),
    ]
