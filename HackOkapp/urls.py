from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'child'

urlpatterns=[
    url(r'^$', views.listView, name='list_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<lost>[-\w]+)/$', views.detailView, name='detail_view'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'
        r'(?P<lost>[-\w]+)/delete/$', views.deleteView, name='delete-view'),
    url(r"^addinfo/$", views.HelperView, name='helper'),
    url(r"^searchinfo/$", views.PoliceView, name='police'),
    url(r"^result/$", views.ResultView, name='result'),
]
