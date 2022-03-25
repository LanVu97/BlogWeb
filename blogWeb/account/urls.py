from django.urls import path
import account.views as views

urlpatterns = [
    path('register/', views.register_request, name='register'),

]