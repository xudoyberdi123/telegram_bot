# Generated by Django 3.1.7 on 2021-03-23 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0020_resumelanguage'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='phone_number',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
