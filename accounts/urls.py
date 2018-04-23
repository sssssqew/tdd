from django.conf.urls import include, url
from django.contrib.auth.views import logout
urlpatterns = [
    url(r'^send_login_email$', 'accounts.views.send_login_email', name='send_login_email'),
    url(r'^login$', 'accounts.views.login', name='login'),
    url(r'^logout$', logout, {'next_page': '/'}, name='logout'),
]
