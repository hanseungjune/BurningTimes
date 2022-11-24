<template>
    <div class="d-flex">
      <img id="left" :src="require(`@/assets/curtain.jpg`)" alt="">
      <img id="right" :src="require(`@/assets/curtain.jpg`)" alt="">
        <br>
        <br>
        <br>
        <div class="circ" v-show="!this.$store.getters.movieVoteAvgListCutting && !this.$store.getters.movieVoteCntListCutting">
          <div class="load">로 딩 중 . . . </div>
          <div class="hands"></div>
          <div class="body"></div>
          <div class="head">
            <div class="eye"></div>
          </div>
        </div>
        <div class="container pt-5" v-show="$store.getters.userPkGetters">
            <br>
            <br>
            <br>
            <div class="row text-center">
              <span class="vote_avg_cnt">이달의 평점 순위</span>
              <br>
              <transition-group name="flip" mode="flip" class="row">
                <MyCard 
                  v-for="movie in voteAvgList"
                  :key = movie.id
                  :movie = movie
                  />
              </transition-group>
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
            <div class="row">
              <h1 class="vote_avg_cnt">이달의 선호도 순위</h1>
              <transition-group mode="out-in" class="row">
                <MyCard 
                v-for="movie in voteCntList"
                :key = movie.id
                :movie = movie
                />
              </transition-group>
            </div>
            <br>
            <br>
            <br>
            <br>
            <br>
            <br>
        </div>
    </div>
</template>

<script>
import MyCard from '@/components/MyCard'

export default {
    name: 'MainPageView',
    components: {
      MyCard,
    },
    data() {
      return {
        userPk : null
      }
    },
    computed: {
      voteAvgList() {
        return this.$store.getters.movieVoteAvgListCutting
      },
      voteCntList() {
        return this.$store.getters.movieVoteCntListCutting
      },
      backgroundImages() {
        return this.$store.getters.backgroundGetters
      },
    },
    async created() {
        console.log(this.$route.path)
        await this.$store.dispatch('getUserPk')
        this.userPk = await this.$store.getters.userPkGetters
        await this.$store.dispatch('getVoteAvgMovieList', this.userPk)
        await this.$store.dispatch('getVoteCntMovieList', this.userPk)
    }
}
</script>

<style>

#left {
  position: fixed;
  width: 50%;
  height: 100%;
  animation: left 4s ease-in-out;
  animation-fill-mode: forwards;
  z-index: 100;
}
#right {
  position: fixed;
  width: 50%;
  height: 100%;
  right: 0;
  animation: right 4s ease-in-out;
  animation-fill-mode: forwards;
  z-index: 100;
}

@keyframes left {
  from {
  }
  50%{
    opacity: 1;
    transform: translateX(0);
  }
  55%{
    opacity: 1;
    transform: translateX(-30%);
  }
  60%{
    opacity: 1;
    transform: translateX(-27%);
  }
  80%{
    opacity: 1;
    transform: translateX(-70%);
  }
  85%{
    opacity: 1;
    transform: translateX(-67%);
  }
  to {
    opacity: 0;
    transform: translateX(-100%);
    visibility: hidden;
  }
}

@keyframes right {
  from {
  }
  50%{
    opacity: 1;
    transform: translateX(0);
  }
  55%{
    opacity: 1;
    transform: translateX(30%);
  }
  60%{
    opacity: 1;
    transform: translateX(27%);
  }
  80%{
    opacity: 1;
    transform: translateX(70%);
  }
  85%{
    opacity: 1;
    transform: translateX(67%);
  }
  to {
    opacity: 0;
    transform: translateX(100%);
    visibility: hidden;
  }
}

/* 로딩 */
.eye{
  width: 20px; height: 8px;
  background-color: rgba(240,220,220,1);
  border-radius:0px 0px 20px 20px;
  position: relative;
  left: 10px; top: 40px;
  box-shadow:  40px 0px 0px 0px rgb(255, 255, 255);              
}

.head{
  backface-visibility: hidden;
  position: relative;
  margin: -250px auto;
  width: 80px; height: 80px;
  background-color: #111;
  border-radius:50px;
  box-shadow: inset -4px 2px 0px 0px rgb(255, 255, 255);
  animation:headAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;
}

.body{ 
  position: relative;
  margin: 90px auto;
  width: 180px; height: 120px;
  background-color: #111;
  border-radius: 50px/25px ;
  box-shadow: inset -5px 2px 0px 0px rgb(255, 255, 255);
  animation:bodyAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;  
}

  @keyframes headAnim{
         0%{ top:0px; }
         50%{ top:10px; }
         100% { top:0px;} 
  }

  @keyframes bodyAnim{
         0%{ top:-5px; }
         50%{ top:10px; }
         100% { top:-5px;} 
  }

.circ{
  backface-visibility: hidden;
  margin: 60px auto;
  width: 180px; height: 180px;
  background-color: #111;
  border-radius: 0px 0px 50px 50px;
  position: relative;
  z-index: -1;  
  left: 0%; top: 20%;
  overflow: hidden;
}

.hands{
  backface-visibility: hidden;
  margin-top: 140px;
  width: 120px;height: 120px;
  position: absolute;
  background-color: #111;
  border-radius:20px;
  box-shadow:-1px -4px 0px 0px rgb(255, 255, 255);
  transform:rotate(45deg);
  top:75%;left: 16%;
  z-index: 1;
  animation:bodyAnim 1.5s infinite alternate;
  animation-timing-function:ease-out;
}

.load{  
  position: absolute;
  width: 7ch; height: 32px;
  text-align: left;
  line-height: 32px;
  margin: -10px auto;
  font-smoothing: antialiased;
  font-family: 'Julius Sans One', sans-serif;
  font-size:28px;
  font-weight:400;
  color:rgb(255, 255, 255);
  left: 2%; top: 5%;
  animation:fontAnim 3.75s infinite;
  animation-timing-function:ease-out;
  word-wrap: break-word;
  display:block;
  overflow: hidden;
}

  @keyframes fontAnim{
        0%{ width:7ch; }
       16%{ width:8ch; }
       32%{ width:9ch; }
       48%{ width:10ch; }
       64%{ width:11ch; }
       80%{ width:12ch; }
     100% { width:13ch;} 
}

/* .vote_avg_cnt{
  width: 800px;
  height: 50px;
  text-align: center;
  font-size: 50px;
  margin-left: 15px;
  margin-bottom: 50px;
  color: white;
  border-radius: 5px;
  z-index: 1;
}



  @keyframes scrolling-left1 {
      0% {transform: translateX(100%);
          -webkit-transform: translateX(100%);}
        100% {transform: translateX(-100%);
            -webkit-transform: translateX(-100%);}
  }
  @keyframes scrolling-left2 {
      0% {transform: translateX(0%);
          -webkit-transform: translateX(0%);}
        100% {transform: translateX(-200%);
            -webkit-transform: translateX(-200%);}
  } */

  /* ㅇㄴㄻㅇㄴㄹㅇㄴㅁㄹ */
  @keyframes tipsy {
    0% {
      transform: translateX(0%) translateY(-40%);
    }
    25% {
      transform: translateX(-5%) translateY(-30%);
    }
    50% {
      transform: translateX(5%) translateY(-30%);
    }
    75% {
      transform: translateX(5%) translateY(-50%);
    }
    100% {
      transform: translateX(-5%) translateY(-50%);
    }
  }

  body {
    font-family: helvetica, arial, sans-serif;
    background-color: #2e2e31;
  }

  .vote_avg_cnt {
    color: #fffbf1;
    text-shadow: 0 20px 25px #2e2e31, 0 40px 60px #2e2e31;
    font-size: 80px;
    font-weight: bold;
    text-decoration: none;
    letter-spacing: -3px;
    margin-bottom: 100px !important;
    position: inherit;
    /* display: flex; */
    text-align: center;
    transform: translateX(0%) translateY(0%);
  }

  .vote_avg_cnt:before,
  .vote_avg_cnt:after {
    content: '';
    padding: .9em .4em;
    position: absolute;
    left: 25%;
    width: 50%;
    top: 25%;
    display: block;
    border: 15px solid red;
    transform: translateX(-50%) translateY(-50%) rotate(0deg);
    animation: 10s infinite alternate ease-in-out tipsy;
  }

  .vote_avg_cnt:before {
    border-color: #d9524a #d9524a rgba(0, 0, 0, 0) rgba(0, 0, 0, 0);
    z-index: -2;
  }

  .vote_avg_cnt:after {
    border-color: rgba(0, 0, 0, 0) rgba(0, 0, 0, 0) #d9524a #d9524a;
    box-shadow: 25px 25px 25px rgba(46, 46, 49, .8);
  }
</style>