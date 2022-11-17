<template>
<div class="d-flex justify-content-center">
  <div class=" overflow-hidden viewport w-75" ref="viewport">
    <div class="row flex-nowrap" id="horizontalScroll" ref="content">
        <MyCard 
            v-for="movie in allMovieList"
            :key = movie.id
            :movie = movie
            />
    </div>
    <i class="bi bi-chevron-left fs-1" @click="clickLeft"></i>
    <i class="bi bi-chevron-right fs-1" @click="clickRight"></i>
  </div>
</div>
</template>

<script>
import ScrollBooster from 'scrollbooster'
import MyCard from '@/components/MyCard'



export default {
    name: 'MovieCartegory',
    components: {
        MyCard,
    },
    data() {
        return {
            cartegory: this.$store.state.cartegory,
            scrollB: null,
        }
    },
    computed: {
        allMovieList() {
            return this.$store.state.movieList
        }
    },
    methods: {
        // 스크롤 부스터
        sb() {
            // refs를 통해서 html요소 정보를 불러올 수 있습니다.
            const viewport = this.$refs.viewport
            const content = this.$refs.content
            // eslint-disable-next-line
            // 리턴으로 스크롤 부스터 객체를 반환
            return new ScrollBooster({
                viewport,
                content,
                direction: "horizontal",
                scrollMode: "transform",
            })
        },
        clickLeft() {
            // 현재 포지션을 받아옴
            const xPosition = this.scrollB.getState().position.x
            // xPosition+this.scrollB.edgeX.from: 스크롤 할 컨텐츠의 전체 넓이
            if (xPosition>-10) {this.scrollB.scrollTo({ x: xPosition+this.scrollB.edgeX.from/12 , y: 0})
                setTimeout(()=>{
                if (this.scrollB.getState().position.x < 0) {
                    this.scrollB.scrollTo({ x: 0 , y: 0})
                }}, 250)
            }
        },
        clickRight() {
            console.log(this.scrollWidth)
            const xPosition = this.scrollB.getState().position.x
            if (xPosition< -this.scrollB.edgeX.from + 10) {
                this.scrollB.scrollTo({ x: xPosition-this.scrollB.edgeX.from/12 , y: 0})
                setTimeout(()=>{
                if (this.scrollB.getState().position.x > -this.scrollB.edgeX.from) {
                    this.scrollB.scrollTo({ x: -this.scrollB.edgeX.from , y: 0})
                }}, 250)
            }
        }
    },
    mounted() {
        // 마운트 될 때 스크롤 함수 동작하게 설정
        // eslint-disable-next-line
        this.scrollB = this.sb()
    }
}
</script>

<style>
.viewport {
    position: absolute;
}
.bi-chevron-left {
    background-color: white;
    opacity: 0.5;
    border-radius: 10%;
    position: absolute;
    top: 43%;
    left: 10px;
}
.bi-chevron-right {
    background-color: white;
    opacity: 0.5;
    border-radius: 10%;
    position: absolute;
    top: 43%;
    right: 10px;
}
</style>