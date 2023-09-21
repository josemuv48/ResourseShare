# Generated by Django 4.2.4 on 2023-08-31 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_rating'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='resourcestag',
            constraint=models.UniqueConstraint(models.F('resources_id'), models.F('tag_id'), name='resource_tag_unique', violation_error_message='Tag already exist for resource'),
        ),
    ]
