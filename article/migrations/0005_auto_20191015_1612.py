# Generated by Django 2.2.5 on 2019-10-15 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20191015_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment_outhor',
            new_name='comment_author',
        ),
    ]