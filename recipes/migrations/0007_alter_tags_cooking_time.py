# Generated by Django 4.1.1 on 2022-12-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_tags_cooking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='cooking_time',
            field=models.CharField(max_length=15),
        ),
    ]
