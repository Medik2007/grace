from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('user/', views.user_view, name='view'),
    path('logout/', views.user_logout, name='logout'), #type:ignore
]
