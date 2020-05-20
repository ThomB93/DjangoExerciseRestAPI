# Generated by Django 3.0.5 on 2020-05-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_auto_20200506_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='CompletedDate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='IsCompleted',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='ManagedReps',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='ManagedSets',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]