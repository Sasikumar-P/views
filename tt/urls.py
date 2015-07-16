from django.conf.urls import patterns, include, url

from ttt import views
from ttt.views import ClassBasedView
from ttt.views import ClassBasedGenericView
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^function/$', views.function_based_view, name='function'),
    url(r'^cbv/$', ClassBasedView.as_view(), name='cbv'),
    url(r'^cbgv/$', ClassBasedGenericView.as_view(), name='cbgv'),
)

