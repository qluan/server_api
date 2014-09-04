from django.conf.urls import include, url
from django.contrib import admin
from server_api.views.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'server_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^time/$', 'server_api.views.views.current_datetime'),
	url(r'^time/plus/(\d{1,2})/$', 'server_api.views.views.hours_ahead'),
]
