"""realproject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from customerapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.dashboard_View),

    url(r'^customerlist/', views.CustomerListView.as_view(),name='customers'),
    url(r'^customerdetails/(?P<pk>\d+)/$', views.CustomerDetailView.as_view(),name='detail'),
    url(r'^create/', views.CustomerCreateView.as_view()),
    url(r'^update/(?P<pk>\d+)/$', views.CustomerUpdateView.as_view()),
    url(r'^delete/(?P<pk>\d+)/$', views.CustomerDeleteView.as_view()),

    url(r'^companylist/', views.CompanyListView.as_view(),name='companies'),
    url(r'^companydetails/(?P<pk>\d+)/$', views.CompanyDetailView.as_view(),name='companydetail'),
    url(r'^createcompany/', views.CompanyCreateView.as_view()),
    url(r'^updatecompany/(?P<pk>\d+)/$', views.CompanyUpdateView.as_view()),
    url(r'^deletecompany/(?P<pk>\d+)/$', views.CompanyDeleteView.as_view()),

    url(r'^blocklist/', views.BlockListView.as_view(),name='blocknames'),
    url(r'^blockdetails/(?P<pk>\d+)/$', views.BlockDetailView.as_view(),name='blockdetail'),
    url(r'^createblock/', views.BlockCreateView.as_view()),
    url(r'^updateblock/(?P<pk>\d+)/$', views.BlockUpdateView.as_view()),
    url(r'^deleteblock/(?P<pk>\d+)/$', views.BlockDeleteView.as_view()),

    url(r'^floorlist/', views.FloorsListView.as_view(),name='floornames'),
    url(r'^floordetails/(?P<pk>\d+)/$', views.FloorsDetailView.as_view(),name='floordetail'),
    url(r'^createfloor/', views.FloorsCreateView.as_view()),
    url(r'^updatefloor/(?P<pk>\d+)/$', views.FloorsUpdateView.as_view()),
    url(r'^deletefloor/(?P<pk>\d+)/$', views.FloorsDeleteView.as_view()),

    url(r'^unitlist/', views.UnitListView.as_view(),name='units'),
    url(r'^unitdetails/(?P<pk>\d+)/$', views.UnitDetailView.as_view(),name='unitdetail'),
    url(r'^createunit/', views.UnitCreateView.as_view()),
    url(r'^updateunit/(?P<pk>\d+)/$', views.UnitUpdateView.as_view()),
    url(r'^deleteunit/(?P<pk>\d+)/$', views.UnitDeleteView.as_view()),

    url(r'^facinglist/', views.FacingListView.as_view(),name='facings'),
    url(r'^facingdetails/(?P<pk>\d+)/$', views.FacingDetailView.as_view(),name='facingdetail'),
    url(r'^createfacing/', views.FacingCreateView.as_view()),
    url(r'^updatefacing/(?P<pk>\d+)/$', views.FacingUpdateView.as_view()),
    url(r'^deletefacing/(?P<pk>\d+)/$', views.FacingDeleteView.as_view()),

    url(r'^unitcreationlist/', views.UnitCreationListView.as_view(),name='unitcreations'),
    url(r'^unitcreationdetails/(?P<pk>\d+)/$', views.UnitCreationDetailView.as_view(),name='unitcreationdetail'),
    url(r'^createunitcreation/', views.UnitCreationCreateView.as_view()),
    url(r'^updateunitcreation/(?P<pk>\d+)/$', views.UnitCreationUpdateView.as_view()),
    url(r'^deleteunitcreation/(?P<pk>\d+)/$', views.UnitCreationDeleteView.as_view()),

    url(r'^amenitieslist/', views.AmenitiesListView.as_view(),name='amenities'),
    url(r'^amenitiesdetails/(?P<pk>\d+)/$', views.AmenitiesDetailView.as_view(),name='amenitiesdetail'),
    url(r'^createamenities/', views.AmenitiesCreateView.as_view()),
    url(r'^updateamenities/(?P<pk>\d+)/$', views.AmenitiesUpdateView.as_view()),
    url(r'^deleteamenities/(?P<pk>\d+)/$', views.AmenitiesDeleteView.as_view()),

    url(r'^unittypelist/', views.UnitTypeListView.as_view(),name='unittype'),
    url(r'^unittypedetails/(?P<pk>\d+)/$', views.UnitTypeDetailView.as_view(),name='unittypedetail'),
    url(r'^createunittype/', views.UnitTypeCreateView.as_view()),
    url(r'^updateunittype/(?P<pk>\d+)/$', views.UnitTypeUpdateView.as_view()),
    url(r'^deleteunittype/(?P<pk>\d+)/$', views.UnitTypeDeleteView.as_view()),

    url(r'^schemelist/', views.SchemeListView.as_view(),name='scheme'),
    url(r'^schemedetails/(?P<pk>\d+)/$', views.SchemeDetailView.as_view(),name='schemedetail'),
    url(r'^createscheme/', views.SchemeCreateView.as_view()),
    url(r'^updatescheme/(?P<pk>\d+)/$', views.SchemeUpdateView.as_view()),
    url(r'^deletescheme/(?P<pk>\d+)/$', views.SchemeDeleteView.as_view()),

    url(r'^unitcostinglist/', views.UnitCostingListView.as_view(),name='unitcosting'),
    url(r'^unitcostingdetails/(?P<pk>\d+)/$', views.UnitCostingDetailView.as_view(),name='unitcostingdetail'),
    url(r'^createunitcosting/', views.UnitCostingCreateView.as_view()),
    url(r'^updateunitcosting/(?P<pk>\d+)/$', views.UnitCostingUpdateView.as_view()),
    url(r'^deleteunitcosting/(?P<pk>\d+)/$', views.UnitCostingDeleteView.as_view()),

]
