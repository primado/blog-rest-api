# Generated by Django 3.2 on 2023-10-27 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='user',
        ),
    ]
