import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_shop.settings'
import django
django.setup()
from django.template import engines
engine = engines['django']
for name in ['admin/login.html', 'registration/login.html', 'admin/logout.html']:
    try:
        template = engine.get_template(name)
        print(name, '=>', template.origin.name)
    except Exception as exc:
        print(name, '=> ERROR', exc)
