# Generated by Django 3.2 on 2021-12-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0034_auto_20211215_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fiche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientId', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
