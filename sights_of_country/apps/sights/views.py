from django.shortcuts import render
from .models import Sight
from django.http import Http404
#HttpResponseRedirect,HttpResponse
# from .models import Sight
# from django.urls import reverse

def index(request):
    sights_list = Sight.objects.order_by('-pub_date')
    return render(request,'sights/list.html',{'sights_list':sights_list})

def detail(request,sight_id):
    try:
        s = Sight.objects.get(id = sight_id)
    except:
        raise Http404('описание объекта не найдено')

    img_list = s.image_set.order_by('id')

    return render(request,'sights/detail.html',{'sight': s,'img_list':img_list})
