<template>
  <nav class="navbar navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <div class="nav">
        <router-link class="navbar-brand" :to="{ name: 'mainpage'}">Ssafy Movie</router-link>
        <NavBarSearch />
      </div>
      <div class="nav">
        <router-link class="nav-link" :to="{ name: 'mainpage'}">Home</router-link>
        <router-link class="nav-link" :to="{ name: 'mainpage'}">Home</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
import NavBarSearch from '@/components/NavBar/NavBarSearch'

export default {
    name: 'NavBar',
    components: {
      NavBarSearch
    }
}
</script>

<style>
  #navbar{
    background-color: #222222;
    z-index: 8;
  }
</style>