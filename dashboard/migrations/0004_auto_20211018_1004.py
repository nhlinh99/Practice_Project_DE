# Generated by Django 3.2.7 on 2021-10-18 03:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_user_rating_information_book_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_rating_information',
            old_name='Book_Info',
            new_name='Book',
        ),
        migrations.RenameField(
            model_name='user_rating_information',
            old_name='User_Info',
            new_name='User',
        ),
        migrations.RenameField(
            model_name='user_rating_information',
            old_name='user_rating',
            new_name='User_Rating',
        ),
    ]