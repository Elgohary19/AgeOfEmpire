# Generated by Django 3.1.7 on 2021-03-10 12:01

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('expansion', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('created_in', models.URLField()),
                ('cost', jsonfield.fields.JSONField()),
                ('build_time', models.IntegerField()),
                ('reload_time', models.FloatField()),
                ('movement_rate', models.FloatField()),
                ('line_of_sight', models.IntegerField()),
                ('hit_points', models.IntegerField()),
                ('attack', models.IntegerField()),
                ('armor', models.CharField(max_length=50)),
                ('attack_bonus', jsonfield.fields.JSONField()),
            ],
        ),
    ]
