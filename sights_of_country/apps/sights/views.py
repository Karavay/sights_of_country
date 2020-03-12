from django.shortcuts import render
from .models import Sight
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

from django.utils import timezone



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

def add_sight_blank(request):
    return render(request,'sights/add_sight_blank.html')

def add_sight(request):
    s = Sight(sight_title = request.POST['name'],
                 sight_description = request.POST['text'],
                 sight_lat = request.POST['lat'],
                 sight_lon = request.POST['lon'],
                 pub_date = timezone.now()
        )
    s.save()
    return HttpResponseRedirect(reverse('sights:index'))

# #map function
# def add_map(request,sight_id):
#     s = Sight.objects.get(id = sight_id)
#     myMap = folium.Map(location=[s.sight_lat,s.sight_lon],tiles = 'CartoDB positron',zoom_start = 5 ,width = 500, heigth = 500)
#
#     folium.Marker(location=[s.sight_lat,s.sight_lon],popup=s.sight_title).add_to(myMap)
#
#     myMap.save('templates/myMap.html')

#   return render(request,'templates/myMap.html')
