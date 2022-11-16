import requests
import json
import pprint

page_num = 1
movie_lst = []

while page_num <= 500:
  URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num}'
  response = requests.get(URL).json()
  movie_lst.append(response['results'])
  page_num += 1

popular_movies = []

for i in range(44):
  for movie in movie_lst[i]:
    movies_dict = dict()
    movies_dict["model"] = 'movies.movie'

    # print(movie)
    fields_dict = dict()
    fields_dict['title'] = movie["title"]
    fields_dict['tmdb_id'] = movie["id"]
    fields_dict['release_date'] = movie["release_date"]
    fields_dict['popularity'] = movie["popularity"]
    fields_dict['vote_count'] = movie["vote_count"]
    fields_dict['vote_average'] = movie["vote_average"]
    fields_dict['overview'] = movie["overview"]
    fields_dict['poster_path'] = movie["poster_path"]
    fields_dict['genres'] = movie["genre_ids"]
    fields_dict['like_users'] = []

    movies_dict['fields'] = fields_dict
    popular_movies.append(movies_dict)

with open("./popular_movies.json", 'w') as f:
  json.dump(popular_movies, f, indent=4, ensure_ascii=False)

pprint.pprint(popular_movies)