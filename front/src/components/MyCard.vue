<template>
<div class="col">
  <b-card class="m-1">
    <b-card-img :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" :alt="movie.title"></b-card-img>
  </b-card>
</div>
</template>

<script>
export default {
    name: 'MyCard',
    props: {
        movie: Object,
    }
}
</script>

<style>

</style>