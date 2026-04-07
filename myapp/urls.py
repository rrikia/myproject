from django.urls import path
from . import views
# the above allows us to configure urls

# list called urlpatterns to contain all the urls of the website
urlpatterns = [
    path('', views.index, name='index'),
    # add another url below
    path('counter', views.counter, name='counter')
]