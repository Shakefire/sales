import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'my_shop.settings'
import django
django.setup()
from django.urls import resolve
from django.template import engines

print('DJANGO_SETTINGS_MODULE=', os.environ['DJANGO_SETTINGS_MODULE'])
print('INSTALLED_APPS=', len(__import__('django.conf').conf.settings.INSTALLED_APPS))
try:
    match = resolve('/login/')
    print('resolve /login/ -> view_name:', match.view_name)
    print('func:', match.func)
    print('namespaces:', match.namespaces)
    print('app_names:', match.app_names)
except Exception as e:
    print('resolve error', type(e).__name__, e)

engine = engines['django']
for name in ['admin/login.html', 'registration/login.html']:
    try:
        template = engine.get_template(name)
        print(name, '=>', template.origin.name)
    except Exception as exc:
        print(name, '=> ERROR', exc)
