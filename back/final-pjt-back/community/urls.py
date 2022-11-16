from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.community_list),
    path('<int:review_pk>/', views.community_detail),
    path('create/', views.create, name='create'),
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'),
    # path('<int:review_pk>/comments/create/<int:parent_comment>/', views.parent_comment, name='parent_comment'),
    # path('<int:review_pk>/like/', views.like, name='like'),
]
