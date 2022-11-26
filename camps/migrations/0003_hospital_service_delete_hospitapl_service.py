# Generated by Django 4.0.8 on 2022-10-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camps', '0002_alter_hospitapl_service_post_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital_service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_location', models.CharField(max_length=100)),
                ('hospital_start_time', models.TimeField()),
                ('hospital_end_time', models.TimeField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': ' Hospital service',
                'ordering': ['-post_date'],
            },
        ),
        migrations.DeleteModel(
            name='Hospitapl_service',
        ),
    ]
