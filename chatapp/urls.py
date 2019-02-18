from django.conf.urls import url, include
from chatapp.views import home, profile, group_details

urlpatterns = [
    url(r'^home/', home, name='home'),
    url(r'^group/(?P<group_id>.+)/$', group_details, name='group_details'),
    url(r'^user/(?P<username>.+)', profile, name='profile'),
    url(r'^accounts/', include('django.contrib.auth.urls'), name='account'),

]