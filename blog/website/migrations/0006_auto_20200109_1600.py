# Generated by Django 3.0.2 on 2020-01-09 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='approved',
            new_name='deleted',
        ),
    ]
