from django.db import models
from jsonfield import JSONField


class Unit(models.Model):
    id = models.AutoField(primary_key=True)
    unit_id = models.IntegerField(default=None, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    expansion = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    created_in = models.CharField(max_length=500)
    cost = JSONField(default={})
    build_time = models.IntegerField(default=None, blank=True, null=True)
    reload_time = models.FloatField(default=None, blank=True, null=True)
    movement_rate = models.FloatField(default=None, blank=True, null=True)
    line_of_sight = models.IntegerField(default=None, blank=True, null=True)
    hit_points = models.IntegerField(default=None, blank=True, null=True)
    range = models.CharField(max_length=50, default=None, blank=True, null=True)
    attack = models.IntegerField(default=None, blank=True, null=True)
    armor = models.CharField(max_length=50)
    attack_bonus = JSONField(default=[])
    accuracy = models.CharField(max_length=50, default=None, blank=True, null=True)
    search_radius = models.IntegerField(default=None, blank=True, null=True)
    blast_radius = models.FloatField(default=None, blank=True, null=True)
    armor_bonus = JSONField(default=[])