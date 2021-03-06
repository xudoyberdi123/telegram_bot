# Generated by Django 3.1.4 on 2020-12-20 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0002_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(db_index=True, max_length=100, verbose_name='rus name')),
                ('name_uz', models.CharField(db_index=True, max_length=100, verbose_name='name_uz')),
                ('ordering', models.PositiveIntegerField(default=0)),
                ('geo_position', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_country', to='geo.country')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='district_region', to='geo.region')),
            ],
        ),
    ]
