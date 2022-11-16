from django.urls import path, include
from . import views

urlpatterns = [
    path('user/<int:user_pk>/', views.user_info),
    path('user/remove/<int:user_pk>/', views.user_delete)
]