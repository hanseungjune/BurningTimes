<template>
  <div style="d-flex" >
    <div id="background-genre" :style="{ backgroundImage: 'url(' + require(`@/assets/genre/${backgroundImages}.png`)+')'}"></div>
        <MovieCartegory />
        <div class="container">
            <div class="row">
                <transition-group name="flip" mode="flip" class="row">
                <MyCard 
                v-for="movie in allMovieList"
                :key = movie.id
                :movie = movie
                />
                </transition-group>
            </div>
        </div>
  </div>
</template>

<script>
import MyCard from '@/components/MyCard'
import MovieCartegory from '@/components/MovieCartegory'

export default {
    name: 'MainPageView',
    components: {
        MyCard,
        MovieCartegory
    },
    computed: {
        allMovieList() {
            return this.$store.getters.movieListCutting
        },
        backgroundImages() {
            return this.$store.getters.backgroundGetters
        }
    },
}
</script>

<style>
#background-genre{
    position: fixed;
    width: 100%;
    height: 100%;
    z-index: -1;
    transition: background-image 0.5s;
    background-position: 0% 0%;
    background-size: 100vw 1920px ;
    filter: blur(4px);
}
/* 슬라이드 페이드 */
.flip-enter-active {
  transition: all 1s ease;
}
.flip-leave-active {
  transition: all .4s ease;
}
.flip-enter{
  transform: translateY(100rem);
  opacity: 0;
} 
.flip-leave-to {
  transform: translateY(100rem);
  opacity: 1;
}
</style>