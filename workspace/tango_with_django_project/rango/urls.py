from django.urls import path
from rango.views import about
from rango import views
from rango.views import show_page

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('page/<slug:page_slug>/', views.show_page, name='show_page'),
]