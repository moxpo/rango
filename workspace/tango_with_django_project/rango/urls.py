from django.urls import path
from rango.views import about
from rango import views
app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', about, name='about'),
]