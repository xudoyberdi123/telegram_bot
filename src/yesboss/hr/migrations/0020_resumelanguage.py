# Generated by Django 3.1.7 on 2021-03-23 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0019_auto_20210323_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResumeLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_language', to='hr.languages')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resume_language_v', to='hr.resume')),
            ],
            options={
                'unique_together': {('resume', 'language')},
            },
        ),
    ]
