# Generated by Django 4.2 on 2023-05-05 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_alter_selectionlist_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selectionlist',
            name='jobs',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobs.jobs'),
        ),
    ]