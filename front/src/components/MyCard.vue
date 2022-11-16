<template>
<div class="col-3">
  <div class="m-1 card">
    <img class="card-img" :src="'https://image.tmdb.org/t/p/original/' + movie?.poster_path" :alt="movie.title">
  </div>
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