<template>
<div class="col-3 my-2">
  <div class="flip-card">
    <div class="flip-card-inner">
      <div class="card h-100 border-0 flip-card-front" id="mycard" @click="modal.show()" >
      <img class="h-100 rounded-start card-img" :src="'https://image.tmdb.org/t/p/original/'+ `${movie?.poster_path}`" alt="">
      </div>
      <div class="flip-card-back rounded border-light p-4 overflow-hidden" id="mycard" @click="modal.show()">
        <h1>{{movie.title}}</h1>
        <br>
        {{movie.overview.slice(0, 190) + "..."}}
      </div>
    </div>
  </div>
  
  <!-- 모달 -->
  <div class="modal fade zoom-in" ref="exampleModal" tabindex="-1" aria-hidden="true"  style="overflow: hidden;">
    <div class="modal-dialog modal-dialog-centered modal-xl">
      <div class="modal-content" style="height: 100vh;">
        <div class="modal-header">
          <h3 class="modal-title" id="exampleModalLabel">{{ movie.title }}</h3>
          <button type="button" class="btn-close" @click="modal.hide()" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          {{ movie.overview }}
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { Modal } from 'bootstrap'

export default {
    name: 'MyCard',
    props: {
        movie: Object,
    },
    data () {
      return {
        modal: null
      }
    },
    mounted() {
      this.modal = new Modal(this.$refs.exampleModal)
    }
}
</script>

<style>
  .card{
    background-size: cover;
    box-shadow: inset 0px 0px 40px 40px #00000065;
  }
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
</style>