from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Movie
from django.contrib.auth import get_user_model
from .serializers import MovieListSerializer, MovieSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         # serializer.save(user=request.user)
    #         return Response(serializer.errors, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        print(serializer.data)
        return Response(serializer.data)

# 영화 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_like(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    user_pk = request.POST.get('userPk')
    user = get_object_or_404(get_user_model(), pk=user_pk)
    if request.POST.get('userPk'):
        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            # movie["like_users"].remove(user)
        else:
            movie.like_users.add(user)
            # movie["like_users"].append(user)
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_204_NO_CONTENT)

# 영화 추천 알고리즘
@api_view(['GET'])
def recommended(request):
    # 사용자가 좋아요를 누른 영화와 같은 장르의 영화 10개를 추천
    # 평점(2)과 좋아요(1) 기준으로 10개 추천
    movies = get_list_or_404(Movie)
    if request.user.is_authenticated:
    # 내가(사용자) 좋아요 누른 영화 가져오고
        me = request.user
        like_movies = me.like_movies.all()
    # 해당 영화와 같은 장르만
        like_dict = dict()
        for like_movie in like_movies:
            for genre in like_movie.genres.all():
                if genre.name not in like_dict:
                    like_dict[genre.name] = 1
                else:
                    like_dict[genre.name] += 1
    # 사용자가 누른 좋아요 영화의 장르 카운팅해서 가장 많이 본 장르 정하고
                max_movie_like = max(like_dict,key=like_dict.get)
    # 그 장르에 해당하는 영화 다 가져오고
        movie_lst = []
        for movie in movies:
            for genre in movie.genres.all():
                if genre.name == max_movie_like:
                    movie_lst.append(movie)
                    # print(movie_lst)

        # print('+++++++++++++++++++++++++')

        new_lst = []
        for like2_movie in movie_lst:
            new_lst.append((
                like2_movie.like_users.count(),
                like2_movie.vote_average,
                like2_movie.title,
                like2_movie.poster_path,
                like2_movie.genres.all()))
        
    # 그 영화들 중에서 좋아요(1), 평점(2) => 최상단 10개를 뽑아오기
        new_lst.sort(key=lambda x : (-x[0], -x[1]))
        new_lst = new_lst[:10]
        context = {
            'new_lst' : new_lst
        }
        return render (request, 'movies/recommended.html', context)
        return Response(context)