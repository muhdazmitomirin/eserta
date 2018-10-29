from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home_penganjur'),

	# http://127.0.0.1:8000/penganjur/aktiviti/add
	path('aktiviti/add/', views.addaktiviti , name='add_aktiviti'),
]