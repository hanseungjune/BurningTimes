<template>
  <div>
    <!-- <img src="@/assets/movie.png" alt="main" class="main-page-scale-img"> -->
    <div class="container">
        <div class="row row-cols-3">
            <MyCard 
            v-for="movie in allMovieList"
            :key = movie.id
            :movie = movie
            />
        </div>
    </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'
export default {
    name: 'MainPageView',
    components: {
        MyCard
    },
    computed: {
        allMovieList() {
            return this.$store.state.movieList
    }
    },
}
</script>

<style>
.main-page-scale-img {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 7;
}
</style>