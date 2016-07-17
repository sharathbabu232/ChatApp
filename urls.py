from django.conf.urls import url, include
from django.contrib import admin, auth
from django.views import static
import settings

from views import index, simple, complex


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Example:
    # (r'^django_jchat/', include('django_jchat.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
    url(r'^$', index),
    url(r'^simple$', simple),
    url(r'^complex/(?P<id>\d)$', complex),
    url(r'^chat/', include('chat.urls', namespace='chat')),    
    url(r'^accounts/login/', admin.site.urls, {'template_name':'login.html'}),
    url(r'^static/(?P<path>.*)$', static.serve,  {'document_root': settings.MEDIA_ROOT})
]
