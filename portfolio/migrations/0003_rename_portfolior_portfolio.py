# Generated by Django 4.1.3 on 2022-11-25 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolior_delete_project'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Portfolior',
            new_name='Portfolio',
        ),
    ]
