# Generated by Django 4.1.1 on 2022-12-01 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='post_date',
            new_name='date_posted',
        ),
    ]
