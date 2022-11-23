<template>
<div>
  <nav class="navbar navbar-dark fixed-top">
    <div class="container-fluid">
      <div class="nav">
        <a class="navbar-brand" id="head">MIcT</a>
      </div>
      <div class="nav">
        <button class="navbar-toggler mx-2" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggleExternalContent" aria-controls="navbarToggleExternalContent" aria-expanded="false" aria-label="Toggle navigation">
          <i class="bi bi-search"></i>
        </button>
        <router-link class="nav-link" :to="{ name: 'main'}">Home</router-link>
        <router-link class="nav-link" :to="{ name: 'allmovie'}">AllMovie</router-link>
        <router-link class="nav-link" :to="{ name: 'genre'}">Genre</router-link>
        <router-link class="nav-link" :to="{ name: 'community'}">Reviews</router-link>
        <router-link class="nav-link" :to="{ name: 'login'}" v-show="!isLogin">Login</router-link>
        <a class="nav-link" v-show="$store.getters.userPkGetters" @click="userLogout">Logout</a>
        <router-link class="nav-link" v-show="!$store.getters.userPkGetters" :to="{ name: 'signup'}">Signup</router-link>
        <router-link class="nav-link" v-if="$store.getters.userPkGetters" :to="{ name: 'userinfo', params: { userPk: isLogin } }">UserInfo</router-link>
      </div>
    </div>
  </nav>
  <div class="collapse" id="navbarToggleExternalContent">
    <div class="d-flex justify-content-end p-3">
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
@import url('https://fonts.googleapis.com/css?family=Black+Han+Sans:400');
@import url('https://fonts.googleapis.com/css?family=Black+Han+Sans&display=swap&subset=korean');
  #head{
    font-family: 'Black Han Sans', sans-serif !important;
    color: #C0FD5B;
  }

  .nav-link{
    color: white !important
  }
  .router-link{
    color: black !important
  }
  .router-link-exact-active {
    color: rgb(9, 27, 192) !important;
    background-color: white;
    border-radius: 10px;
  }
  #navbarToggleExternalContent {
    position: fixed;
    right: 0;
    width: 100%;
    z-index: 10;
  }
  .navbar{
    background-color: #FF4301;
    animation: navfade 5s;
  }
  @keyframes navfade {
    from {
      background-color: rgb(143, 38, 38);
    }
    70% {
      background-color: rgb(143, 38, 38);
    }
    to {
      
    }
  }
</style>
