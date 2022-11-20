<template>
<div class="col-3 my-2">
  <div>
    <div>
      <div class="card" id="mycard" :style="{ backgroundImage: 'url(' +'https://image.tmdb.org/t/p/original/'+ `${movie?.poster_path}` + ')'}" :class="{ 'is-clicked' : is_clicked }" @click="clickCard">
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      <br>
      </div>
    </div>
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
  border: 10px blue solid !important;
  border-radius: 2px !important;
}
  .card{
    background-size: cover;
    box-shadow: inset 0px 0px 40px 40px #00000065;
  }
  /* #mycard:hover {
    transform: scale(1.1);
    transition: transform 330ms ease-in-out;
    z-index: 1;
  } */
</style>