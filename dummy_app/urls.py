from django.urls import path
from dummy_app import views

app_name = 'dummy_app'

urlpatterns = [
    # path('login/', views.login, name='login'),
    # path('profile/', views.profile, name='profile'),
    path('', views.dummy, name='dummy')
]
