<template>
<div>
  <h1>UserInfo</h1>
  <h2>{{ userInformation?.username }}</h2>
  <button class="btn btn-danger" v-if="$route.params.userPk === $store.state.userPk" @click="removeUser">회원탈퇴</button>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'UserInfoPageView',
    data() {
        return {
            userInformation: null,
        }
    },
    methods: {
        getUserInfo() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                // url: `${DJANGO_API_URL}/accounts/user/`,
                // headers: {
                //     Authorization: `Token ${this.$store.state.token.key}`
                // }
            })
            .then(res => {
                this.userInformation = res.data
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        removeUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/accounts/user/remove/${this.$store.state.userPk}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                }
            })
            .then(res => {
                console.log(res)
                this.$cookies.remove('token')
                this.$store.state.userPk = null
                this.$router.push({name: 'main'})
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        }
    },
    created() {
        this.getUserInfo()
    }
}
</script>

<style>

</style>