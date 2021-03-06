# Generated by Django 3.1.7 on 2021-03-05 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_vacancies'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacanciCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies_categories', to='hr.category')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacancies_categories_v', to='hr.vacancies')),
            ],
            options={
                'unique_together': {('vacancy', 'category')},
            },
        ),
    ]
