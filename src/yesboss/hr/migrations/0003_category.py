# Generated by Django 3.1.7 on 2021-03-04 20:14

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import yesboss.base.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(db_index=True, editable=False, null=True)),
                ('name', models.JSONField(default=yesboss.base.fields.lang_dict_field)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_main', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(db_index=True, default=False)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prcategorychildren', to='hr.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
