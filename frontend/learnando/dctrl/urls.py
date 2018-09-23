from django.urls import path

from . import views

urlpatterns = [
    # ex: /dctrl/
    path('', views.index, name='index'),        
    # ex: /dctrl/27fc95e5a3/start/
    # ex: dctrl/27fc95e5a3/stop/
    path('<container_id>/<action>/', views.container, name='container'),
]