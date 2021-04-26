# Generated by Django 3.1.7 on 2021-03-04 20:13

from django.db import migrations, models
import yesboss.base.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.JSONField(default=yesboss.base.fields.lang_dict_field)),
                ('alias', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]
