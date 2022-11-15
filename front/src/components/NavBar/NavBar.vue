<template>
  <div id="navbar" >
    <b-navbar>
      <b-navbar-brand>
        <router-link :to="{ name: 'mainpage'}">Ssafy Movie</router-link>
      </b-navbar-brand>
      <NavBarSearch />
      <b-navbar-nav class="ml-auto">
        <b-nav-item>
          <router-link :to="{ name: 'mainpage'}">Home</router-link>
        </b-nav-item>
        <b-nav-item>
          <router-link :to="{ name: 'mainpage'}">About</router-link>
        </b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </div>
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
    position: relative;
    background-color: #222222;
    z-index: 8;
  }
</style>