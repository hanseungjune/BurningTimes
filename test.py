import requests
import json
import pprint

page_num = 1
movie_lst = []

while page_num <= 499:
  URL = f'https://api.themoviedb.org/3/movie/popular?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR&page={page_num}'
  response = requests.get(URL).json()
  results = response['results']
  for result in results:
    if result['popularity'] < 100:
      continue
    else:
      movie_lst.append(result)
  page_num += 1

# pprint.pprint(movie_lst)
# print(len(movie_lst[0]))

popular_movies = []
popular_movies_actors = []

for movie in movie_lst:
    try:
        print(movie)
        ACTORS_URL = f'https://api.themoviedb.org/3/movie/{int(movie["id"])}/credits?api_key=0802a25be8939d20e57e4d6621c62927&language=ko-KR'
        response1 = requests.get(ACTORS_URL).json()
        # popular_movies_actors.append(response1["cast"])

        cnt = 0
        for cast in response1["cast"]:
            if cnt == 5:
              break

            if cast["known_for_department"] != "Acting":
              continue
            else:
                actor_dict = dict()
                actor_dict["model"] = "movies.actor"
                actor_dict["pk"] = cast["id"]

                fields_dict = dict()
                fields_dict["name"] = cast["name"]
                actor_dict['fields'] = fields_dict
                cnt += 1
            popular_movies_actors.append(actor_dict)
        print(len(actor_dict))
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

with open("./popular_movies_actors.json", 'w', encoding='UTF-8') as f:
  json.dump(popular_movies_actors, f, indent=4, ensure_ascii=False)

pprint.pprint(popular_movies_actors)