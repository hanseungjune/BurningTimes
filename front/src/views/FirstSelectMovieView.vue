<template>
  <div>
    <h1>좋아하시는 영화를 선택 해주세요!</h1>
    <div class="container">
      <button @click="updateSelect">더 찾아보기!</button>
      <button @click="likeMovieEnd">선택완료!</button>
        <div class="row">
            <transition-group name="flip" mode="flip" class="row">
            <FirstSignCard 
              v-for="movie in allMovieList"
              :key = movie.id
              :movie = movie
              @movieId="selectMovie"
            />
            </transition-group>
        </div>
    </div>
  </div>
</template>

<script>
import FirstSignCard from '@/components/FirstSign/FirstSignCard.vue'
import axios from 'axios'

export default {
    name: 'FirstSelectMovieView',
    components: {
      FirstSignCard
    },
    data() {
      return {
        selected: []
      }
    },
    computed: {
        allMovieList() {
            return this.$store.getters.selectMovieCutting
        },
    },
    methods: {
      updateSelect() {
        this.$store.commit('GET_FIRST_SELECT', this.selected)
      },
      selectMovie(id) {
        if (this.selected.includes(id)) {
          this.selected = this.selected.filter(el => el !== id)
        } else {
          this.selected.push(id)
        }
      },
      likeMovieEnd() {
        const likemovies = this.selected
        const DJANGO_API_URL = 'http://127.0.0.1:8000'
        axios({
            method: 'post',
            url: `${DJANGO_API_URL}/api/accounts/user/${this.$store.getters.userPkGetters}/likemovies/`,
            data: {
                likemovies
            },
        })
        .then(() => {
          this.$router.push({name: 'main'})
        })
        .catch(err => {
            console.log(err.response)
            console.log(err.request)
            console.log(err.message)
        })
      }
    },
    created() {
      this.$store.commit('GET_FIRST_SELECT', this.selected)
    }
}
</script>

<style>

</style>