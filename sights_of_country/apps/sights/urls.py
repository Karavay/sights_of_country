from . import views
from django.urls import path

app_name = 'sights'

urlpatterns = [
    path('<int:sight_id>/',views.detail,name='detail'),
    path('',views.index,name='index'),
    path('add_sight_blank',views.add_sight_blank,name='add_sight_blank'),
]
