import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import userAccount from './modules/userAccount'
import _ from 'lodash'
// import VueCookies from 'vue-cookies'

const DJANGO_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: [],
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
    backgroundGetters(state) {
      return state.backgroundImg
    }
  },
  mutations: {
    GET_MOVIE_LIST(state, payload) {
      state.movieList = payload
      state.genreSelectList = payload
    },
    SELECT_GENRE(state, genreId) {
      if (genreId !== 0) {
        state.genreSelectList = state.movieList.filter((el) => {
        if (el.genres.includes(genreId)) {
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
    }
  },
  actions: {
    getMovieList(context) {
      // const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
      // const API_URL =`https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
      axios({
        method: 'get',
        url: `${DJANGO_API_URL}/api/v1/movies/`
      })
        .then(res => {
          context.commit('GET_MOVIE_LIST', res.data)
        })
        .catch(err => console.log(err))
    }, 
  },
  modules: {
    userAccount: userAccount,
  }
})
