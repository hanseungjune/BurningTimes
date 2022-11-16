from django.urls import path
from . import views

urlpatterns = [
    path('community/', views.community_list),
    path('community/<int:review_pk>/', views.community_detail),
    path('community/comments/', views.comment_list),
    path('community/comments/<int:comment_pk>/', views.comment_detail),
    path('community/<int:review_pk>/comments/', views.comment_create),
    path('community/<int:review_pk>/comments/<int:parent_comment_pk>/', views.parent_comment),
    # path('community/<int:review_pk>/comments/<int:parent_comment>/', views.parent_comment),
]
