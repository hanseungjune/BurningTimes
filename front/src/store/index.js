import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import userAccount from './modules/userAccount'
// import VueCookies from 'vue-cookies'

// const DJANGO_API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movieList: []
  },
  getters: {
  },
  mutations: {
    GET_MOVIE_LIST(state, payload) {
      state.movieList = payload
    },
  },
  actions: {
    getMovieList(context) {
      const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
      const API_URL =` https://api.themoviedb.org/3/movie/popular?api_key=${TMDB_API_KEY}&language=ko-KR&page=1`
      axios({
        method: 'get',
        url: API_URL
      })
        .then(res => {
          context.commit('GET_MOVIE_LIST', res.data.results)
        })
        .catch(err => console.log(err))
    }, 
  },
  modules: {
    userAccount: userAccount,
  }
})
