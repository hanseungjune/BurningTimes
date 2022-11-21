<template>
<div class="col-3 my-2">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="card h-100 border-0 flip-card-front" id="mycard" @click="modal.show()" >
      <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/original/'+ `${movie?.poster_path}`" alt="">
      </div>
      <div class="flip-card-back rounded border-light p-4 overflow-hidden" id="mycard" @click="modal.show()">
        <h1>{{movie.title}}</h1>
        <h2>{{movie.vote_average}}</h2>
        <br>
        {{movie.overview.slice(0, 190) + "..."}}
      </div>
    </div>
  </div>
  
  <!-- Detail -->
  <div class="modal fade zoom-in" ref="exampleModal" tabindex="-1" aria-hidden="true"  style="overflow: hidden;">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content" style="height: 100vh;">
        <div class="modal-header">
          <span class="modal-title" id="exampleModalLabel"></span>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <div class="container">
            <div id="Detail_title_vote" class="row">
              <div id="detail_title" class="col-3">
                {{ movie?.title }}
              </div>
              <div id="avg_cnt_like_set" class="col-3">
                <div class="avg_cnt_like">
                  평점<br>
                  {{movie?.vote_average}}
                </div>
                <div class="avg_cnt_like">
                  평론수<br>
                  {{movie?.vote_count}}
                </div>
                <div class="avg_cnt_like" @click="ToLiking" :class="{'selected':like_choiced}">
                  좋아요<br>
                  <i class="bi bi-hand-thumbs-up-fill"></i>
                </div>
              </div>
            </div>

            <div class="row">
              <div class="col-4">
                <img id="detail_img" :src="'https://www.themoviedb.org/t/p/w600_and_h900_bestv2' + `${movie?.poster_path}`">
                
              </div>

            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { Modal } from 'bootstrap'
import axios from 'axios'
const DJANGO_API_URL = 'http://127.0.0.1:8000'
// import Vue from 'vue'

export default {
    name: 'MyCard',
    props: {
        movie: Object,
    },
    data () {
      return {
        modal: null,
        userPk : null,
        like_choiced : false,
      }
    },
    mounted() {
      this.modal = new Modal(this.$refs.exampleModal)
    },
    methods : {
      ToLiking() {
        this.$store.dispatch('getUserPk')
        this.userPk = this.$store.getters.userPkGetters
        const payload = {
          'userPk' : this.userPk,
          'moviePk' : this.movie.id
        }
        axios({
          method: 'post',
          url: `${DJANGO_API_URL}/api/v1/movies/${payload.userPk}/like/`,
          headers: {
            Authorization: `Token ${this.$cookies.get("token")}`
          },
          data : {
            movie: this.movie.id
          }
        })
        .then(res => {
            console.log(res.data)
            if (this.like_choiced === false) {
              this.like_choiced = true
            }
            else {
              this.like_choiced = false
            }
            this.$store.commit('TO_LIKING', payload)
          })
          .catch(err => console.log(err))
      }
    }
  }

</script>

<style>
  /* #mycard:hover {
    transform: scale(1.1);
    transition: transform 330ms ease-in-out;
    z-index: 1;
  } */

  /* The flip card container - set the width and height to whatever you want. We have added the border property to demonstrate that the flip itself goes out of the box on hover (remove perspective if you don't want the 3D effect */
  .flip-card {
    background-color: transparent;
    width: 100%;
    height: 100%;
    perspective: 1000px; /* Remove this if you don't want the 3D effect */
  }

  /* This container is needed to position the front and back side */
  .flip-card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.4s ease-in-out;
    transform-style: preserve-3d;
  }

  /* Do an horizontal flip when you move the mouse over the flip box container */
  .flip-card:hover .flip-card-inner {
    transform: rotateY(180deg);
  }

  /* Position the front and back side */
  .flip-card-front, .flip-card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden; /* Safari */
    backface-visibility: hidden;
  }

  /* Style the front side (fallback if image is missing) */
  .flip-card-front {
    background-color: #bbb;
    color: black;
  }

  /* Style the back side */
  .flip-card-back {
    position: fixed;
    top: 0;
    background-color: black;
    color: white;
    transform: rotateY(180deg);
  }
  /* 모달 애니메이션 */
  .modal.fade .modal-dialog{
    -webkit-transform: translate(0,0)!important;
    transform: translate(0,0)!important;
  }

  .zoom-in {
    transform: translateY(100vh)!important;
    opacity: 1!important;
    -webkit-transition: .5s all ease-in-out!important;
    -moz-transition: .5s all ease-in-out!important;
    -ms-transition: .5s all ease-in-out!important;
    -o-transition: .5s all ease-in-out!important;
    transition: .5s all ease-in-out!important;
    display: block !important;
  }

  .zoom-in.show {
    opacity: 1!important;
    transform: translateY(0)!important;
    transform:none!important;
  }

  .modal-title {
    font-weight: 900;
    font-size: 25px;
    margin-left: 20px;
  }

  
  #avg_cnt_like_set {
    width: 400px;
    display: flex;
  }
  
  .avg_cnt_like {
    width: 250px;
    height: 80px;
    border: 1px solid green;
    background-color: green;
    color: white;
    padding-top: 15px;
    text-align: center;
    border-radius: 50%;
    margin: 20px;
  }

  #Detail_title_vote {
    display: flex;
    justify-content: space-between;
  }

  #detail_title {
    margin-top: 20px;
    margin-left: 10px;
    font-size: 30px;
    font-weight: 900;
  }

  #detail_img {
    width: 300px;
    height: 450px;
  }

  .selected {
    color: black;
  }
</style>