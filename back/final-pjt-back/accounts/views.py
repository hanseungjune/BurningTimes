from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserProfileSerializer, UserUpdateSerializer, UserDeleteSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET', 'PUT'])
def user_info (request, user_pk):
    if request.method == "GET":
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
    elif request.method == "PUT":
        user = get_object_or_404(get_user_model(), pk=user_pk)
        serializer = UserUpdateSerializer(user, data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    serializer = UserDeleteSerializer(user, data = request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_follow(request, followed_pk, following_pk):
    request.POST.get('pk')
    target = get_object_or_404(get_user_model(), pk=followed_pk)
    follower = get_object_or_404(get_user_model(), pk=following_pk)
    if following_pk != followed_pk:
        if target.followers.filter(pk=follower.pk).exists():
            target.followers.remove(follower)
        else:
            target.followers.add(follower)
    return Response(status=status.HTTP_202_ACCEPTED)