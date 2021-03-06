# Generated by Django 3.1.7 on 2021-03-04 20:16

from django.db import migrations, models
import yesboss.base.fields
import yesboss.hr.models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_schedules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.JSONField(default=yesboss.hr.models.default_experience_val)),
                ('name', models.JSONField(default=yesboss.base.fields.lang_dict_field)),
                ('alias', models.CharField(max_length=32, unique=True)),
                ('sort_order', models.IntegerField(db_index=True, null=True)),
            ],
        ),
    ]
