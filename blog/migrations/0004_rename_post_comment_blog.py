# Generated by Django 4.2 on 2023-05-04 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_email_comment_name_comment_website'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='blog',
        ),
    ]