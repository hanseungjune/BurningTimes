<template>
<div>
  <nav class="navbar navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <div class="nav">
        <router-link class="nav-link" :to="{ name: 'test'}">Test</router-link>
        <router-link class="navbar-brand" :to="{ name: 'main'}">Ssafy Movie</router-link>
        
      </div>
      <div class="nav">
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="bi bi-search"></i>
        </button>
        <router-link class="nav-link" :to="{ name: 'main'}">Home</router-link>
        <router-link class="nav-link" :to="{ name: 'genre'}">Genre</router-link>
        <router-link class="nav-link" :to="{ name: 'login'}" v-show="!isLogin">Login</router-link>
        <a class="nav-link" v-show="$store.getters.userPkGetters" @click="userLogout">Logout</a>
        <router-link class="nav-link" v-show="!$store.getters.userPkGetters" :to="{ name: 'signup'}">Signup</router-link>
        <router-link class="nav-link" v-if="$store.getters.userPkGetters" :to="{ name: 'userinfo', params: { userPk: isLogin } }">UserInfo</router-link>
      </div>
    </div>
  </nav>
  <div class="collapse pt-5" id="navbarToggleExternalContent">
    <div class="d-flex justify-content-end bg-dark p-3">
      <NavBarSearch class="d-flex" />
    </div>
  </div>
</div>
</template>

<script>
import NavBarSearch from '@/components/NavBar/NavBarSearch'

export default {
    name: 'NavBar',
    components: {
      NavBarSearch
    },
    computed: {
      isLogin() {
        return this.$store.getters.userPkGetters
      }
    },
    methods: {
      userLogout() {
        this.$store.dispatch('userLogout')
        this.$router.push({name: 'main'})
      }
    }
}
</script>

<style>
  #navbar{
    background-color: #222222;
    z-index: 8;
  }
  
</style>