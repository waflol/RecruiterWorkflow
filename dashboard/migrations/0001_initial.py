# Generated by Django 4.1.3 on 2022-11-26 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField()),
            ],
        ),
    ]