from django.shortcuts import render
from .models import Monitor, File

ikon = 'files/favicon2.ico'


def home(request):
    dat = []
    dat.append({
        'name': 'Этап 1',
        'url': 'etap1'
    })
    dat.append({
        'name': 'Этап 2',
        'url': 'etap2'
    })
    return render(request, 'home.html', {'data': dat, 'ikon': ikon})


def etap1(request):
    # add()

    global ikon
    monitors = Monitor.objects.all()
    data = []
    for monitor in monitors:
        files = File.objects.filter(monitor=monitor).order_by('order')
        type = str(files[0].file)[-3:]
        if len(files) > 1:
            carousel = True
        else:
            carousel = False
        data.append({
            'name': monitor.name,
            'files': files,
            'carousel': carousel,
            'type': type
        })
    return render(request, 'etap1.html', {'data': data, 'ikon': ikon})


def etap2(request):
    monitors = Monitor.objects.all()
    data = []
    for monitor in monitors:
        files = File.objects.filter(monitor=monitor).order_by('order')
        type = str(files[0].file)[-3:]
        if len(files) > 1:
            carousel = True
        else:
            carousel = False
        data.append({
            'name': monitor.name,
            'files': files,
            'carousel': carousel,
            'type': type
        })
    return render(request, 'etap2.html', {'data': data, 'ikon': ikon})


def add():
    m1 = Monitor.objects.create(name='меню 1')
    File.objects.create(name='menu1.mp4', file='/files/menu1.mp4', monitor=m1)
    m2 = Monitor.objects.create(name='меню 2')
    File.objects.create(name='menu2.jpg', file='files/menu2.jpg', monitor=m2)
    r = Monitor.objects.create(name='реклама')
    File.objects.create(name='adv1.jpg', file='files/sadv1.jpg', monitor=r, duration=15, order=0)
    File.objects.create(name='adv2.jpg', file='files/sadv2.jpg', monitor=r, duration=15, order=1)
