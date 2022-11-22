<template>
  <div>
    <br>
    <div class="container d-flex justify-content-center align-items-center">
      <br>
      <br>
      <div class="card text-center userinfo_box">
          <div class="card-header">
              <h1>MyPage</h1>
          </div>
          <div class="card-body d-flex flex-column align-items-center">
              <h2><b>{{ userInformation?.username }}</b>'s ROOM (●'◡'●)</h2>
              <!-- <div class="follow_box">
                followings : {{this.userInformation.followings.length()}}<br>
                followers : {{this.userInformation.followers.length()}}
              </div> -->
              <div>
                <span href="#" @click="favoriteGenre" class="btn btn-primary">당신이 가장 좋아하는 장르는?</span>
              </div>
              <div id="favorite_genre_box">
                <button type="button" v-if="favorite_genre" @click="goToGenre" class="btn btn-outline-secondary">{{favorite_genre}}</button>
                <button type="button" v-if="!favorite_genre" class="btn btn-outline-secondary"> 장르를 클릭하면 해당 페이지로 넘어가요! d=====(￣▽￣*)b </button>
              </div>
          </div>
          <div class="card-footer text-muted d-flex justify-content-between">
            <button class="btn btn-secondary" v-show="$store.getters.userPkGetters" @click="updateShow=!updateShow">UPDATE</button>
            <button class="btn btn-success" @click="followUser" v-show="$store.getters.userPkGetters"><i id="user_follow" class="bi bi-hand-index-thumb-fill"></i> FOLLOW</button>
            <button class="btn btn-danger" v-show="$store.getters.userPkGetters" @click="removeUser">USERBYE</button>
          </div>
      </div>
      <br>
      <div style="height:30%" class="card text-center" v-show="updateShow">
        <div class="card-header">
          UserInfo UPDATE
        </div>
        <div class="card-body d-flex flex-column align-items-center">
          <div id="userInfoUpdate">
            <form @submit.prevent="updateUser"  v-show="updateShow">
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="userFirstName" placeholder="FirstName을 입력하세요" v-model="userFirstName">
                    <label for="userFirstName">FirstName</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="userLastName" placeholder="LastName을 입력하세요" v-model="userLastName">
                    <label for="userLastName">LastName</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="userEmail" placeholder="Email을 입력하세요" v-model="userEmail">
                    <label for="userEmail">Email</label>
                </div>
                <div>
                </div>
                <div class="card-footer text-muted">
                  <input class="btn btn-primary" type="submit" value="수정">
                </div>
            </form>
          </div>
        </div>
      </div>
      <br>
    </div>
      <div class="container pt-5" v-show="$store.getters.userPkGetters">
        <div class="row">
          <div id="like_movies_title" class="col-3">LIKE MOVIE</div>
          <br>
          <div class="col-3"></div><div class="col-3"></div><div class="col-3"></div>
        </div>
        <div class="row">
          <transition-group name="flip" mode="flip" class="row">
            <MyCard 
            v-for="movie in getLikeMovieListShow"
            :key = movie.id
            :movie = movie
            />
          </transition-group>
        </div>
      </div>
      <br>
    </div>
</template>

<script>
import MyCard from '@/components/MyCard.vue'

import axios from 'axios'
export default {
    name: 'UserInfoPageView',
    components: {
      MyCard
    },
    data() {
        return {
            userInformation: null,
            updateShow: false,
            userFirstName: null,
            userLastName: null,
            userEmail: null,
            favorite_genre: null,
            genre_category: [
                {
                    "id": 12,
                    "name": "모험"
                },
                {
                    "id": 28,
                    "name": "액션"
                },
                {
                    "id": 16,
                    "name": "애니메이션"
                },
                {
                    "id": 35,
                    "name": "코미디"
                },
                {
                    "id": 80,
                    "name": "범죄"
                },
                {
                    "id": 99,
                    "name": "다큐멘터리"
                },
                {
                    "id": 18,
                    "name": "드라마"
                },
                {
                    "id": 10751,
                    "name": "가족"
                },
                {
                    "id": 14,
                    "name": "판타지"
                },
                {
                    "id": 36,
                    "name": "역사"
                },
                {
                    "id": 27,
                    "name": "공포"
                },
                {
                    "id": 10749,
                    "name": "로맨스"
                },
                {
                    "id": 10402,
                    "name": "음악"
                },
                {
                    "id": 9648,
                    "name": "미스터리"
                },
                {
                    "id": 878,
                    "name": "SF"
                },
                {
                    "id": 10770,
                    "name": "TV 영화"
                },
                {
                    "id": 53,
                    "name": "스릴러"
                },
                {
                    "id": 10752,
                    "name": "전쟁"
                },
                {
                    "id": 37,
                    "name": "서부"
                }
            ],
        }
    },
    computed: {
      getLikeMovieListShow() {
        return this.$store.getters.moviesLikeListGetters
      }
    },
    methods: {
        getUserInfo() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                // url: `${DJANGO_API_URL}/accounts/user/`,
                // headers: {
                //     Authorization: `Token ${this.$store.state.token.key}`
                // }
            })
            .then(res => {
                this.userInformation = res.data
                this.userFirstName = res.data.first_name
                this.userLastName = res.data.last_name
                this.userEmail = res.data.email
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        removeUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/accounts/user/remove/${this.$store.getters.userPkGetters}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                data: {
                    is_active: false
                }
            })
            .then(res => {
                console.log(res)
                this.$cookies.remove('token')
                this.$store.state.userAccount.userPk = null
                this.$router.push({name: 'main'})
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        followUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/accounts/user/follow/${this.userInformation.id}/${this.$store.getters.userPkGetters}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get("token")}`
<<<<<<< HEAD
                }
=======
                },
>>>>>>> 1b1a9fc8e823cfd737907ec04e8932bb0f8df9aa
            })
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        updateUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const first_name = this.userFirstName
            const last_name = this.userLastName
            const email = this.userEmail
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                data: {
                    first_name, last_name, email
                }
            })
            .then(res => {
              this.updateShow = false
              console.log(res.data)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        favoriteGenre() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/movies/${this.$route.params.userPk}/favorite_genre/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
            })
            .then(res => {
              this.genre_category.forEach((genre) => {  
                if (genre.id === res.data.favorite_genre_num){
                  this.favorite_genre = genre.name
                  console.log(123124132521)
                }
              })
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        goToGenre() {
          this.$router.push({name:'genre'})
        }
    },
    async created() {
        await this.getUserInfo()
        await this.$store.dispatch('getUserPk')
        this.userPk = await this.$store.getters.userPkGetters
        await this.$store.dispatch('getLikeMovieList', this.userPk)
    }
}
</script>

<style>
  #favorite_genre_box {
    padding: 10px 30px;
    width: 50%;
    font-size: 20px;
  }
  .follow_box{
    border: 1px solid black;
    border-radius: 5px;
    padding: 10px 40px;
    margin-top: 5px;
    margin-bottom: 20px;
    width: 50%;
    font-size: 20px;
  }
  .userinfo_box {
    width: 70% !important;
  }
  .like_movies {
    margin-top: 20px;
  }

  #like_movies_title{
  width: 300px;
  height: 50px;
  text-align: center;
  font-size: 30px;
  padding-top: 5px;
  margin-left: 15px;
  margin-bottom: 50px;
  background-color: black;
  color: white;
  border-radius: 5px;
}
</style>