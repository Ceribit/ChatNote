from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name ='notes'),
    path('notes/<int:id>/edit', views.edit_note, name = 'edit_note'),
    path('delete_note/<int:id>', views.delete_note, name ='delete_note'),
    path('logout/', auth_views.logout, {'next_page':'/'}, name = 'logout' ),
    path('search/', views.search, name = 'search'),
    path('friends/', views.friends, name = 'friends'),
    re_path(r'^profile/(?P<username>\w{0,30})/$',
            views.profile, name='profile' ),
]
