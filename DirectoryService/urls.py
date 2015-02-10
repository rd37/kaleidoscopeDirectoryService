'''
Created on Feb 9, 2015

@author: ronaldjosephdesmarais
'''
from django.conf.urls import patterns, include, url

import DirectoryService.views as views

urlpatterns = patterns('',
    url(r'^register/(?P<json_msg>.+)', views.register, name='register'),
    url(r'^deregister/(?P<json_msg>.+)', views.deregister, name='deregister'),
    url(r'^listservices', views.listservices, name='listservices'),
    url(r'^getservice/(?P<json_msg>.+)', views.getservice, name='getservice'),
) 