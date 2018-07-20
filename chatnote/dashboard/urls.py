from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name ='note'),
    path('logout/', auth_views.logout, {'next_page':'/'}, name = 'logout' ),
    path('search/', views.search, name = 'search'),
    path('friends/', views.friends, name = 'friends'),
    re_path(r'^profile/(?P<username>\w{0,30})/$',
            views.profile, name='profile' ),
]
