from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name ='home'),
    path('logout/', auth_views.logout, {'next_page':'/'}, name = 'logout' ),
    #path('signup/', views.signup, name='signup')
]
