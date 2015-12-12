from django.conf.urls import url
from django_taiga_reports import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]