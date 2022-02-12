from django.urls import path

from myproject_test import views

urlpatterns = [
    path('', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/', views.toRegister_view),
    path('register/', views.Register_view),
]