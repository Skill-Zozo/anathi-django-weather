from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog.models import Register

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Register.objects.all(), template_name = "blog/register.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Register,template_name='blog/register.html'))]
