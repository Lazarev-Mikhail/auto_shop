from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexTemplate.as_view(), name='index'),
    path('catalog/all_cars', views.show_all_cars, name='all_cars'),
    path('catalog/<slug:slug_auto>', views.show_one_auto, name='one_car'),
    path('brend', views.ListBrend.as_view(), name='brends'),
    path('brend/<str:brend_auto>', views.show_brend_car, name='brend_car'),
    path('contact', views.contact, name='contact'),
]
