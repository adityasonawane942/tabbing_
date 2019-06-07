from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.WelcomePage.as_view(), name='welcome'),
    path('register/', views.UserFormView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='home/login.html'), name='login'),
    path('addtournament/', views.TournamentCreate.as_view(), name='add-tournament'),
    path('homepage/', views.Homepage.as_view(), name='homepage'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    re_path(r'^(?P<pk>[0-9]+)/participants/$', views.Participants.as_view(), name='participants'),
    re_path(r'^(?P<pk>[0-9]+)/motions/$', views.Motions.as_view(), name='motions'),
    re_path(r'^(?P<pk>[0-9]+)/settings/$', views.Settings.as_view(), name='settings'),
    re_path(r'^(?P<pk>[0-9]+)/rounds/$', views.Rounds.as_view(), name='rounds'),
    re_path(r'^(?P<pk>[0-9]+)/breaks/$', views.Breaks.as_view(), name='breaks'),
    re_path(r'^(?P<pk>[0-9]+)/standings/$', views.Standings.as_view(), name='standings'),
    re_path(r'^(?P<pk>[0-9]+)/breakrounds/$', views.BreakRounds.as_view(), name='breakrounds'),
]
