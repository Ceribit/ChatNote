from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('logout/', auth_views.logout, {'next_page':'/'}, name = 'logout' ),
    re_path(r'^profile/(?P<username>\w{0,30})/$', views.profile, name='profile' ),
    path('search/', views.search, name = 'search'),
]
