from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^login/$', views.loginUser, name='loginUser'),
    url(r'^register/$', views.register, name='register'),
	url(r'^logout/$', views.logout_view, name='logout_view'),
	url(r'^actual_weather/$', views.actual_weather, name='actual_weather'),
	
]
