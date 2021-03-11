# Generated by Django 3.1.7 on 2021-03-10 13:40

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('retriveApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='accuracy',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='armor_bonus',
            field=jsonfield.fields.JSONField(default=[]),
        ),
        migrations.AddField(
            model_name='unit',
            name='blast_radius',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='search_radius',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='unit',
            name='unit_id',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='unit',
            name='cost',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='unit',
            name='created_in',
            field=models.CharField(max_length=500),
        ),
    ]