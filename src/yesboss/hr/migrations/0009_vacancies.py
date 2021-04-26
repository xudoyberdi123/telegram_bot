# Generated by Django 3.1.7 on 2021-03-04 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import yesboss.hr.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0001_initial'),
        ('geo', '0003_district'),
        ('hr', '0008_resumecategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancies',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('subcats', models.JSONField(blank=True, default=yesboss.hr.models.vacancy_default_subcats)),
                ('file_type', models.SmallIntegerField(blank=True, null=True)),
                ('file_path', models.CharField(blank=True, max_length=600, null=True)),
                ('salary', models.JSONField(blank=True, default=yesboss.hr.models.vacancy_default_salary)),
                ('age', models.JSONField(blank=True, default=yesboss.hr.models.vacancy_default_experience)),
                ('languages', models.JSONField(blank=True, null=True)),
                ('requirements', models.CharField(blank=True, max_length=600, null=True)),
                ('views_count', models.IntegerField(default=0, editable=False)),
                ('contact_count', models.IntegerField(default=0, editable=False)),
                ('gender', models.IntegerField(default=0, editable=False)),
                ('created_dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_vacancies', to='hr.category')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_vacancies', to='company.companies')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='district_vacancies', to='geo.district')),
                ('experience', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='experience_vacancies', to='hr.experience')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='position_vacancies', to='hr.positions')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='region_vacancies', to='geo.region')),
                ('schedule', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedules_vacancies', to='hr.schedules')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_vacancies', to='hr.statuses')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_vacancy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
