import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import _ from 'lodash'
// import VueCookies from 'vue-cookies'

const DJANGO_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

const movie = {
  state: {
    movieList: [],
    movieVoteAvgList: null,
    movieVoteCntList: null,
    genreSelectList: null,
    firstSelectList: null,
    backgroundImg: '0',
  },
  getters: {
      getAllMovies(state) {
        return state.movieList
      },
      selectMovieCutting(state) {
        return state.firstSelectList
      },
      movieListCutting: (state) => {
        return _.sampleSize(state.genreSelectList, 20)
      },
      movieVoteAvgListCutting: (state) => {
        return _.sampleSize(state.movieVoteAvgList, 12)
      },
      movieVoteCntListCutting: (state) => {
        return _.sampleSize(state.movieVoteCntList, 12)
      },
      genreSelectListgetters: (state) => {
        return state.genreSelectList
      },
      backgroundGetters(state) {
        return state.backgroundImg
      },
      
  },
  mutations: {
      GET_MOVIE_LIST(state, payload) {
        state.movieList = payload
        state.genreSelectList = payload
      },
      GET_VOTE_AVG_MOVIE_LIST(state, payload) {
        state.movieVoteAvgList = payload
      },
      GET_VOTE_CNT_MOVIE_LIST(state, payload) {
        state.movieVoteCntList = payload
      },
      SELECT_GENRE(state, genreId) {
        if (genreId !== 0) {
          state.genreSelectList = state.movieList.filter((el) => {
            let isGenre = false
            el.genres.forEach(genre => {
              if (genre.id === genreId) {
                isGenre = true
              }
            })
            if (isGenre) {
              return el
            }
        })
        } else {
          state.genreSelectList = _.sampleSize(state.movieList, 20)
        }
      },
      BG_GET(state, genreId) {
        state.backgroundImg = genreId
      },
      GET_FIRST_SELECT(state, nums) {
        state.firstSelectList = state.movieList.slice(nums-8, nums)
      },
      TO_LIKING(state, payload) {
        state.movieList.forEach((movie) => {
          if (movie.id == payload.moviePk){
            // console.log(12323534252)
            if (movie.like_users.includes(payload.userPk)){
              movie.like_users = movie.like_users.filter((el)=> {
                return el !== payload.userPk
              })
            }else{
              // console.log(movie)
              movie.like_users.push(payload.userPk)
            }
          }
        })
      },
  },
  actions: {
    getMovieList(context) {
        // const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
        // const API_URL =`https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
        return axios({
          method: 'get',
          url: `${DJANGO_API_URL}/api/v1/movies/`
        })
          .then(res => {
            context.commit('GET_MOVIE_LIST', res.data)
            context.commit('GET_FIRST_SELECT', 8)
          })
          .catch(err => console.log(err))
      }, 
      getVoteAvgMovieList(context, userPk) {
        return axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${userPk}/recommended_vote_average/`,
          headers: {
            Authorization: `Token ${Vue.$cookies.get("token")}`
          }
        })
          .then(res => {
            context.commit('GET_VOTE_AVG_MOVIE_LIST', res.data)
          })
          .catch(err => console.log(err))
      },
      getVoteCntMovieList(context, userPk) {
        return axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${userPk}/recommended_vote_count/`,
          headers: {
            Authorization: `Token ${Vue.$cookies.get("token")}`
          }
        })
          .then(res => {
            context.commit('GET_VOTE_CNT_MOVIE_LIST', res.data)
          })
          .catch(err => console.log(err))
      },
  },
  modules: {
  }
}

export default movie