<template>
  <div>
    <div class="container">
        <div class="row row-cols-3">
            <MyCard 
            v-for="movie in searchMovieList"
            :key = movie.id
            :movie = movie
            />
        </div>
    </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'
import axios from 'axios'
export default {
    name: 'SearchPageView',
    components: {
        MyCard
    },
    data() {
      return {
        searchMovieList: [],
        searchMovieKeyword: this.$route.params.keyword
      }
    },
    methods: {
      searchMovie(searchMovieKeyword) {
        const keyword = searchMovieKeyword
        const TMDB_API_KEY = process.env.VUE_APP_TMDBKEY
        const API_URL =`https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&language=ko-KR&query=${keyword}&page=1&include_adult=false`
        axios({
          method: 'get',
          url: API_URL
        })
          .then(res => {
            this.searchMovieList = res.data.results
          })
          .catch(err => console.log(err))
      }
    },
    watch: {
      searchMovieKeyword (value, oldValue) {
        oldValue
        this.searchMovie(value)
      }
    },
    created() {
      this.searchMovie(this.searchMovieKeyword)
    },
    beforeRouteUpdate(to, from, next) {
      console.log(to.params.keyword)
      this.searchMovieKeyword = to.params.keyword
      next()
    }
}
</script>

<style>

</style>