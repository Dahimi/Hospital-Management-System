# Generated by Django 3.2 on 2021-12-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0026_bed_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='isAffected',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologue', 'Cardiologue'), ('Dermatologues', 'Dermatologues'), ("Spécialistes en médecine d'urgence", "Spécialistes en médecine d'urgence"), ('Allergologues/Immunologues', 'Allergologues/Immunologues'), ('Anesthésiologistes', 'Anesthésiologistes'), ('Chirurgiens du côlon et du rectum', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
    ]
