"""renty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from detail import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='API Renty Docs')


urlpatterns = [
    # path('', views.CarView.as_view()),
    path('admin/', admin.site.urls),
    url(r'^rentals/', views.RentalView.as_view()),
    # url(r'^cars/$', views.CarView.as_view()),
    url(r'^cars/(?P<carid>[-\w]+)/$', views.CarView.as_view()),
    url(r'^cars/search$', views.CarSearchView.as_view(), name='car-search'),
    url(r'^docs/', schema_view),
    url(r'^booking/', views.ReservationList.as_view()),
    # url(r'^cars/search$from=<from>&to=<to>&type=<type>&pickup=<pickup>', views.CarView.as_view()),

    url(r'^cars/token$', views.ReservationView.as_view())
]

# https://renty-web.herokuapp.com/cars/search?from=2018-11-15&to=2018-11-17&type=lujo&pickup=aeropuerto
