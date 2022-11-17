from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_list),
    path('<int:review_pk>/', views.community_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:review_pk>/comments/', views.comment_create),
    path('<int:review_pk>/comments/<int:parent_comment_pk>/', views.parent_comment),
    # path('community/<int:review_pk>/comments/<int:parent_comment>/', views.parent_comment),
]
