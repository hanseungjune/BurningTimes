<template>
<div class="col-3 my-2">
    <div class="card h-100" id="FirstSigncard"  :class="{ 'is-clicked' : is_clicked }" @click="clickCard">
    <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/original/'+ `${movie?.poster_path}`" alt="">
    </div>
 </div>
</template>

<script>

export default {
    name: 'FirstSignCard',
    props: {
        movie: Object,
    },
    data () {
      return {
        is_clicked : false
      }
    },
    methods: {
      clickCard() {
        this.is_clicked = !this.is_clicked
        this.$emit('movieId', this.movie.id)
      }
    }
}
</script>

<style>
.is-clicked{
  opacity: 0.2 !important;
  transition: all 0.3s ease-in-out
}
#FirstSigncard {
  opacity: 1;
  transition: all 0.3s ease-in-out
}
</style>