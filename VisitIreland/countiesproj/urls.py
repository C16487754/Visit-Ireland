from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf.urls.i18n import i18n_patterns

from accounts import views as accounts_views
from counties import views

urlpatterns = []

urlpatterns += i18n_patterns(
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^counties/(?P<pk>\d+)/$', views.county_attractions, name='county_attractions'),

    url(r'^counties/(?P<pk>\d+)/attractions/(?P<attraction_pk>\d+)/$', views.attraction_comments, name='attraction_comments'),
    url(r'^counties/(?P<pk>\d+)/attractions/(?P<attraction_pk>\d+)/reply/$', views.reply_attraction, name='reply_attraction'),
    url(r'^admin/', admin.site.urls),
)
