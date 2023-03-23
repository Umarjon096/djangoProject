import os
import django
from test1.models import Monitor, File

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
django.setup()

m1 = Monitor.objects.create(name='меню 1')
File.objects.create(name='menu1.mp4', file='files/menu1.mp4', monitor=m1)
m2 = Monitor.objects.create(name='меню 2')
File.objects.create(name='menu2.jpg', file='files/menu2.jpg', monitor=m2)
r = Monitor.objects.create(name='реклама')
File.objects.create(name='adv1.jpg', file='files/adv1.jpg', monitor=r, duration=15, order=0)
File.objects.create(name='adv2.jpg', file='files/adv2.jpg', monitor=r, duration=15, order=1)
