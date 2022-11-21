<template>
  <div>
    <h1>리뷰게시판입니다</h1>
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
            .then(res => this.communityList = res.data)
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        }
    },
    created() {
        this.getCommunityList()
    }
}
</script>

<style>

</style>