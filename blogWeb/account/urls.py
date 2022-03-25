from django.urls import path
import account.views as views

urlpatterns = [
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path("logout", views.logout_request, name= "logout"),
]