<template>
  <nav class="navbar navbar-dark bg-dark fixed-top">
    <div class="container-fluid">
      <div class="nav">
        <router-link class="nav-link" :to="{ name: 'test'}">Test</router-link>
        <router-link class="navbar-brand" :to="{ name: 'main'}">Ssafy Movie</router-link>
        <NavBarSearch />
      </div>
      <div class="nav">
        <router-link class="nav-link" :to="{ name: 'main'}">Home</router-link>
        <router-link class="nav-link" :to="{ name: 'login'}" v-if="!isLogin">Login</router-link>
        <a class="nav-link" v-if="isLogin" @click="userLogout">Logout</a>
        <router-link class="nav-link" v-if="!isLogin" :to="{ name: 'signup'}">Signup</router-link>
        <router-link class="nav-link" v-if="isLogin" :to="{ name: 'userinfo', params: { userPk: isLogin } }">UserInfo</router-link>
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