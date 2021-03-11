from django_tables2.export.views import ExportMixin
import django_tables2 as tables



class TableView(ExportMixin, tables.Table):
    # id = tables.TemplateColumn('<span>{{record.unit_id}}</span>')
    name = tables.TemplateColumn('<span>{{record.name}}</span>')
    description = tables.TemplateColumn('<span>{{record.description}}</span>')
    expansion = tables.TemplateColumn('<span>{{record.expansion}}</span>')
    age = tables.TemplateColumn('<span>{{record.age}}</span>')
    created_in = tables.TemplateColumn('<a target="_blank" href="{{record.created_in}}"><span>Click Here</span></a>')
    cost = tables.TemplateColumn('<span>{% for k,v in record.cost.items %} {{k}}: {{v}}{% endfor %}</span>')
    build_time = tables.TemplateColumn('<span>{{record.build_time}}</span>')
    reload_time = tables.TemplateColumn('<span>{{record.reload_time}}</span>')
    movement_rate = tables.TemplateColumn('<span>{{record.movement_rate}}</span>')
    line_of_sight = tables.TemplateColumn('<span>{{record.line_of_sight}}</span>')
    hit_points = tables.TemplateColumn('<span>{{record.hit_points}}</span>')
    range = tables.TemplateColumn('<span>{{record.range}}</span>')
    attack = tables.TemplateColumn('<span>{{record.attack}}</span>')
    armor = tables.TemplateColumn('<span>{{record.armor}}</span>')
    # I hide these fields from table to make style better

    # attack_bonus = tables.TemplateColumn('<span>{{record.attack_bonus}}</span>')
    # accuracy = tables.TemplateColumn('<span>{{record.accuracy}}</span>')
    # search_radius = tables.TemplateColumn('<span>{{record.search_radius}}</span>')
    # blast_radius = tables.TemplateColumn('{% if record.blast_radius %}<span>{{record.blast_radius}}</span>{% else %}{% endif %}')
    # armor_bonus = tables.TemplateColumn('<span>{{record.armor_bonus}}</span>')
    exclude_columns = ("buttons", )

# '<a target="_blank" class="btn btn-primary" data-toggle="modal" data-target="#exampleModalScrollable href="">{{record.Title}}</a>'