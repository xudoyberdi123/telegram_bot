# Generated by Django 3.1.7 on 2021-03-05 18:54

from django.db import migrations, models
import yesboss.hr.models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0013_vacancies_position_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancies',
            name='file_path',
            field=models.FileField(blank=True, max_length=300, null=True, upload_to=yesboss.hr.models.get_file_folder),
        ),
    ]
