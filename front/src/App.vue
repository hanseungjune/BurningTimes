<template>
  <div id="app">
    <NavBar />
    <!-- 슬라이드 트랜지션 -->
    <transition  mode="out-in">
      <router-view style="margin-top: 56px; min-height: 100vh"/>
    </transition>

    <FooterFoot/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar/NavBar.vue'
import FooterFoot from '@/components/FooterFoot/FooterFoot.vue'

export default {
    name: 'App',
    components: {
      NavBar,
      FooterFoot,
    },
    created() {
        this.$store.dispatch('getMovieList')
        if (this.$cookies.get('token')) {
          this.$store.dispatch('getUserPk')
        }
    },
    
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

/* 슬라이드 페이드 */
.v-enter-active {
  transition: all .3s ease;
}
.v-leave-active {
  transition: all .4s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.v-enter{
  transform: translateX(-50%);
  opacity: 0;
} 
.v-leave-to {
  transform: translateX(50%);
  opacity: 0;
}
</style>
