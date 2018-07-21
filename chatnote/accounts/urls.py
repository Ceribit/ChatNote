from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('settings/', views.settings, name='settings'),
    path('add_friend/<int:id>', views.send_request, name='send_request'),
    path('notifications', views.notifications, name='notifications'),
    path('notifications/complete_request/<int:id>', views.complete_request, name='complete_request'),

]
