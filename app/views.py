from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    return render(request,'display_topics.html',context=d)

def display_webpages(request):
     QLWO=Webpage.objects.all()
     d={'webpages':QLWO}

     return render(request,'display_webpages.html',context=d)

def display_accessrecords(request):
     QLAO=AccessRecord.objects.all()
     d={'accessrecords': QLAO}
     return render(request,'display_accessrecords.html',context=d)


def insert_topic(request):
     tn=input('enter topic name')
     NTO=Topic.objects.get_or_create(topic_name=tn)[0]
     NTO.save()
     return HttpResponse('Topic is created')

def insert_webpage(request):
     tn=input('enter tn')
     n=input('enter name')
     u=input('enter url')
     e=input('enter email')

     TO=Topic.objects.get(topic_name=tn)
     NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u,email=e)[0]
     NWO.save()
     return HttpResponse('Webpage is created')


def insert_access(request):
     pk=int(input('enter pk value of webpage'))
     a=input('enter author')
     d=input('enter date')

     WO=Webpage.objects.get(pk=pk)
     NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
     NAO.save()
     return HttpResponse('Access is created')