# Generated by Django 3.1.7 on 2021-03-23 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0016_auto_20210321_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='firstname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='lastname',
            field=models.CharField(blank=True, max_length=33, null=True),
        ),
        migrations.AddField(
            model_name='resume',
            name='middlename',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
