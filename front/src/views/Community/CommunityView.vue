<template>
  <div>
    <h1>리뷰게시판입니다</h1>
    <router-link class="btn btn-success" :to="{ name: 'communitycreate'}">리뷰 작성</router-link>
    <div 
        v-for="review in communityList"
        :key="review.id"
    >
        {{ review.id }} {{ review.movie.title }} {{review.title}} {{ review.user.username }} {{ review.created_at.slice(0,10)}}
        <button class="btn btn-primary" @click="moveToDetail(review.id, review.movie.id)">상세</button>
        <br>
        <br>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityView',
    data() {
        return{
            communityList: null
        }
    },
    methods: {
        getCommunityList() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/v1/community/`
            })
            .then(res => {this.communityList = res.data})
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        moveToDetail(reviewid, movieid) {
            this.$router.push({ name : 'communitydetail', params : {reviewid: reviewid, movieid: movieid}})
        }
    },
    created() {
        this.getCommunityList()
    }
}
</script>

<style>

</style>