from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserProfileSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
def user_info (request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserProfileSerializer(user)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)