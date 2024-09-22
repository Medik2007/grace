from django.urls import path

from . import views


app_name = 'dress'
urlpatterns = [
    path('', views.index, name='index'),
    path('bucket/', views.bucket, name='bucket'), #type:ignore
    path('service.php/', views.service, name='service'), #type:ignore
    path('<str:id>/', views.view, name='view'), #type:ignore
]
