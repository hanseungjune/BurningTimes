# final_project

SSAFY 최종 관통 프로젝트

## 0. Install

---

- django

```python
python manage.py makemigrations
python manage.py migration
pyhton manage.py loaddata popular_actors.json popular_genres.json popular_movies.json 
```

## 1. 팀원 정보 및 업무 분담 내역

---

#### 한승준(팀장)



#### 배상준(팀원)

- 백엔드
  
  - dj-rest-auth를 활용한 account기능
  
  - accounts App 구성 (view, model, serializer)
  
  - django setting 수정

- 프론트엔드
  
  - 프론트 뷰 구조 설계
  
  - 스켈레톤 Vue페이지 구성
    
    - 검색
      
      - Vue의 필터를 활용한 검색
    
    - 장르별 페이지
      
      - 가로스크롤 기능(Scrollbooster)
      
      - Scrollbooster를 활용한 이동버튼
    
    - 리뷰
    
    - 전체 영화페이지
      
      - 정렬 기능
      
      - 페이지네이션
    
    - 전체적으로 사용할 카드 컴포넌트
      
      - 플립카드
      
      - Bootstrap5 Modal in Vue2
    
    - 네브바
  
  - 애니메이션 구현
    
    - Vue transition
    
    - keyframe을 활용한 animation & transition



## 2. 목표 서비스 구현 및 실제 구현 정도

---

## 3. 데이터베이스 모델링

---

![project_detail.jpg](C:\Users\multicampus\Downloads\project_detail.jpg)

> Account App
> 
>     accounts/login/ :로그인 (토큰발급)
> 
>     accounts/logout/ : 로그아웃 (토큰삭제)
> 
>     accounts/signup/ : 회원가입 (토큰발급)
> 
>     api/accounts/user/int:user_pk/ : get => 유저 정보 put => 유저 정보 수정  
>     ** data { first_name, last_name, email } **
> 
>     api/accounts/user/remove/int:user_pk/ : 유저삭제(현재 active = 0, remove 주석)
> 
>     api/accounts/user/follow/int:followed_pk/int:following_pk/ : 유저 팔로우
> 
>     api/accounts/user/int:user_pk/likemovies/ : 회원가입한 유저 좋아요  
>     ** data { likemovies : ?? } **



> Movie App
> 
> api/v1/movies/ : 영화 전체 목록 가져오기  
> api/v1/movies/int:movie_pk : 특정 영화 가져오기  
> api/v1/movies/int:movie_pk/like/ : 특정 영화 좋아요  
> ** user_pk = request.POST.get('userPk') **
> 
> api/v1/movies/<int: user_pk>/like_movies/ : 좋아요한 영화 가져오기  
> ** like_movies = user.like_movies.all() **
> 
> api/v1/movies/int:user_pk/recommended_vote_average/ : 평점 순으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **recommend_movie_sorted_final_lst**
> 
> api/v1/movies/int:user_pk/recommended_vote_count/ : 투표수 순으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **recommend_movie_sorted_final_lst**
> 
> api/v1/movies/int:user_pk/recommended_random/ : 랜덤으로 가져오기(좋아요 가장 많이 누른 장르 관련 영화 모두 가져오고 정렬함)  
> **random_lst**



> Community App
> 
> api/v1/community/ : 게시글 전체 들고오기  
> 
> api/v1/community/movie/<int:movie_pk>/  
> : 특정 영화의 게시글 전체 보기 또는 생성(GET, POST)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> 
> api/v1/community/movie/<int:movie_pk>/review/<int:review_pk>/  
> : 특정 영화의 특정 게시글 가져오기 또는 삭제 또는 수정(GET, DELETE,PUT)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> 
> api/v1/community/movie/<int:movie_pk>/review/<int:review_pk>/review_recommended/<int:user_pk>/ : 특정 영화의 특정 게시글을 추천하기  
> 
> : 특정 리뷰에 댓글 전체 보기 또는 생성(GET, POST)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user')) **  
> ** parent_comment = get_object_or_404(Comment, pk=request.POST.get('parent')) **  
> 
> api/v1/community/review/<int:review_pk>/comments/<int:comment_pk>/  
> : 특정 리뷰의 특정 댓글 보기 또는 삭제 또는 생성(GET, DELETE,PUT)  
> ** user = get_object_or_404(get_user_model(), pk=request.POST.get('user'))**  
> **parent_comment = get_object_or_404(Comment, pk=request.POST.get('parent'))**



## 4. 영화 추천 알고리즘에 대한 기술적 설명

---

## 5. 서비스 대표 기능에 대한 설명

---

DB에 저장되어있는 모든 영화들을 조회 가능하고, 좋아요, 평점, 개봉날짜 순으로 정렬과 장르별 선택 기능을 동시에 할 수 있음.

장르별로 DB에 저장된 영화들을 랜덤으로 찾는 기능

자신이 좋아요를 누른 영화를 기반으로 추천영화를 메인에 띄워주는 기능

## 6. 기타 (느낀점, 후기)

---

배상준 : 
