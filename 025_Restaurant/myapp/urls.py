# restaurant/urls.py

from django.urls import path
from myapp.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',                          home,             name='home'),
    path('menu/',                     menu,             name='menu'),
    path('menu/<int:pk>/',            menu_item_detail, name='menu_item_detail'),
    path('specials/',                 specials,         name='specials'),
    path('order/',                    order,            name='order'),
    path('order/place/',              order_place,      name='order_place'),
    path('order/confirm/<int:pk>/',   order_confirm,    name='order_confirm'),
    path('order/track/<int:pk>/',     order_track,      name='order_track'),
    path('about/',                    about,            name='about'),
    path('contact/',                  contact,          name='contact'),
    path('contact/submit/',           contact_submit,   name='contact_submit'),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)