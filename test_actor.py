import requests
import json
import pprint

page_num1 = 1
movie_lst1 = []

while page_num1 <= 499:
  URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num1}'
  response1 = requests.get(URL).json()
  results1 = response1['results']
  for result in results1:
    if result['popularity'] < 100:
      continue
    else:
      movie_lst1.append(result)
  page_num1 += 1

# pprint.pprint(movie_lst)
# print(len(movie_lst[0]))

popular_movies1 = []
popular_movies_actors1 = []

for movie in movie_lst1:
    try:
        ACTORS_URL = f'https://api.themoviedb.org/3/movie/{int(movie["id"])}/credits?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR'
        response2 = requests.get(ACTORS_URL).json()
        # popular_movies_actors.append(response1["cast"])

        cnt1 = 0
        for cast1 in response2["cast"]:
            if cnt1 == 5:
              break
            if cast1["known_for_department"] != "Acting":
              continue
            else:
                actor_dict1 = dict()
                actor_dict1["pk"] = cast1["id"]
                cnt1 += 1

            popular_movies_actors1.append(actor_dict1)

    except KeyError:
        movies_dict = dict()
        continue
    except UnicodeEncodeError:
        movies_dict = dict()
        continue
    except FileNotFoundError:
        movies_dict = dict()
        continue
    except KeyboardInterrupt:
        movies_dict = dict()
        continue

pprint.pprint(popular_movies_actors1)
print(len(popular_movies_actors1))

#######################################################

page_num = 1
movie_lst = []

while page_num <= 499:
    URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num}'
    response = requests.get(URL).json()
    movie_lst.append(response['results'])
    page_num += 1

popular_movies = []
popular_movies_actors = []

for i in range(len(movie_lst)-1):
    for movie in movie_lst[i]:
        try:
            ACTORS_URL = f'https://api.themoviedb.org/3/movie/{movie["id"]}/credits?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR'
            response3 = requests.get(ACTORS_URL).json()
            casts = response3["cast"]
                
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
            
            cast_id_lst = []
            for cast in casts:
              if cast["known_for_department"] == "Acting":
                for actor in popular_movies_actors1:
                  if actor['pk'] != cast['id']:
                    continue
                  else:
                    # not in 으로 처리해야 id가 중복으로 들어가지 않는다(작업해야댐)
                    cast_id_lst.append(cast["id"])
            fields_dict['actors'] = cast_id_lst

            fields_dict['like_users'] = []
            movies_dict['fields'] = fields_dict
            popular_movies.append(movies_dict)
            pprint.pprint(popular_movies)

        except KeyError:
            movies_dict = dict()
            continue
        except UnicodeEncodeError:
            movies_dict = dict()
            continue
        except FileNotFoundError:
            movies_dict = dict()
            continue
        except KeyboardInterrupt:
            movies_dict = dict()
            continue

with open("./popular_movies.json", 'w', encoding='UTF-8') as f:
  json.dump(popular_movies, f, indent=4, ensure_ascii=False)

pprint.pprint(popular_movies)