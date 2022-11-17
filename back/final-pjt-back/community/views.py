from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Review, Comment
from .serializers import ReviewSerializer, ReviewListSerializer, CommentSerializer

# 쓸일 없는데 일단 살려둠(모든 게시판에서 리뷰 달기)
@api_view(['GET', 'POST'])
def community_list(request):
    if request.method == 'GET':
        reviews = Review.objects.order_by('-pk')
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def community_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
      serializer = ReviewSerializer(review, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 여기서부터 댓글 기능
@api_view(['GET'])
def comment_list(request):
  comments = get_list_or_404(Comment)
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)
  
@api_view(['GET','DELETE','PUT'])
def comment_detail(request, comment_pk):
  comment = get_object_or_404(Comment, pk=comment_pk)
  if request.method == 'GET':
    serializer = CommentSerializer(comment)
    return Response(serializer.data)

  elif request.method == 'DELETE':
    comment.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  elif request.method == 'PUT':
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)

@api_view(['POST'])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      if request.POST.get('parent'):
        # userPk
          parent_comment = get_object_or_404(Comment, pk = request.POST.get('parent'))
          serializer.save(review=review, parent_comment = parent_comment)
      else:
        serializer.save(review=review)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE','PUT'])
def parent_comment(request, review_pk, parent_comment_pk):
    # review = get_object_or_404(Review, pk=review_pk)
    parent_comment = get_object_or_404(Comment, pk=parent_comment_pk)
    if request.method == 'GET':
      serializer = CommentSerializer(parent_comment)
      return Response(serializer.data)
    
    elif request.method == 'DELETE':
      parent_comment.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
      serializer = CommentSerializer(parent_comment, data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)

# 게시글 좋아요...?
# @require_POST
# def like(request, review_pk):
#     if request.user.is_authenticated:
#         review = get_object_or_404(Review, pk=review_pk)
#         user = request.user

#         if review.like_users.filter(pk=user.pk).exists():
#             review.like_users.remove(user)
#             is_liked = False
#         else:
#             review.like_users.add(user)
#             is_liked = True
#         context = {
#             'is_liked':is_liked,
#             'review_like_users_count':review.like_users.count()
#         }
#         return JsonResponse(context)
#         # return redirect('community:index')
#     return redirect('accounts:login')

