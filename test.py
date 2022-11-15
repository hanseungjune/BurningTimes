import requests
import json
import pprint

page_num = 1
movie_lst = []

while page_num <= 500:
  URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num}'
  response = requests.get(URL).json()
  movie_lst.append(response)
  page_num += 1

pprint.pprint(movie_lst)