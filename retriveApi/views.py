from django.shortcuts import render
from .models import Unit
from .table import TableView
import requests


def get_api_data(request):
    api_body = requests.get('https://age-of-empires-2-api.herokuapp.com/api/v1/units').json()
    units = api_body["units"]

    for item in units:
        if not Unit.objects.filter(unit_id=item['id']).exists():
            unit = Unit()
            unit.unit_id = item['id']
            unit.name = item['name']
            unit.description = item['description']
            unit.expansion = item['expansion']
            unit.age = item['age']
            unit.created_in = item['created_in']
            unit.cost = item.get('cost', None)
            unit.reload_time = item.get('reload_time', None)
            unit.build_time = item.get('build_time', None)
            unit.movement_rate = item.get('movement_rate', None)
            unit.line_of_sight = item.get('line_of_sight', None)
            unit.hit_points = item.get('hit_points', None)
            unit.armor = item.get('armor', None)
            unit.range = item.get('range', None)
            unit.attack = item.get('attack', None)
            unit.attack_bonus = item.get('attack_bonus', None)
            unit.accuracy = item.get('accuracy', None)
            unit.armor_bonus = item.get('armor_bonus', None)
            unit.search_radius = item.get('search_radius', None)
            unit.blast_radius = item.get('blast_radius', None)
            unit.save()


def main(request):
    get_api_data(request)
    kwargs = {}
    if request.GET.get('unit_name', None):
        unit_name = request.GET['unit_name']
        kwargs['name__icontains'] = unit_name

    unit = Unit.objects.filter(**kwargs)

    if not kwargs: uni = 0
    elif kwargs: uni = 1
    export_obj = TableView(unit)
    context = {
        'export_obj': export_obj,
        'unit': unit,
        'uni': uni
    }
    return render(request, 'home.html', context)

