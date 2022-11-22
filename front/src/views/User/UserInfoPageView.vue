<template>
<div class="container">
    <br>
    <br>
    <div class="card text-center">
        <div class="card-header">
            <h1>MyPage</h1>
        </div>
        <div class="card-body">
            <h2><b>{{ userInformation?.username }}</b>'s ROOM (●'◡'●)</h2>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
            <a href="#" class="btn btn-primary">Go somewhere</a>
        </div>
        <div class="card-footer text-muted">
            2 days ago
        </div>
    </div>
  <h1>UserInfo</h1>
  <h2>{{ userInformation?.username }}</h2>
  <button class="btn btn-danger" v-show="$store.getters.userPkGetters" @click="removeUser">회원탈퇴</button>
  <button class="btn btn-primary" v-show="$store.getters.userPkGetters" @click="updateShow=!updateShow">정보 수정</button>
  <button class="btn btn-success" @click="followUser" v-show="$store.getters.userPkGetters">팔로우</button>
  <div id="userInfoUpdate">
    <form @submit.prevent="updateUser"  v-show="updateShow">
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="userFirstName" placeholder="FirstName을 입력하세요" v-model="userFirstName">
            <label for="userFirstName">FirstName</label>
        </div>
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="userLastName" placeholder="LastName을 입력하세요" v-model="userLastName">
            <label for="userLastName">LastName</label>
        </div>
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="userEmail" placeholder="Email을 입력하세요" v-model="userEmail">
            <label for="userEmail">Email</label>
        </div>
        <input class="btn btn-primary" type="submit" value="수정">
    </form>
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'UserInfoPageView',
    data() {
        return {
            userInformation: null,
            updateShow: false,
            userFirstName: null,
            userLastName: null,
            userEmail: null,
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
                this.userFirstName = res.data.first_name
                this.userLastName = res.data.last_name
                this.userEmail = res.data.email
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
                url: `${DJANGO_API_URL}/api/accounts/user/remove/${this.$store.getters.userPkGetters}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                data: {
                    is_active: false
                }
            })
            .then(res => {
                console.log(res)
                this.$cookies.remove('token')
                this.$store.state.userAccount.userPk = null
                this.$router.push({name: 'main'})
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        followUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get("token")}`
                },
                data: {

                }
            })
            .then(res => {
                console.log(res.data)
            })
            .catch(err => {
                console.log(err.response)
                console.log(err.request)
                console.log(err.message)
            })
        },
        updateUser() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const first_name = this.userFirstName
            const last_name = this.userLastName
            const email = this.userEmail
            axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/accounts/user/${this.$route.params.userPk}/`,
                headers: {
                    Authorization: `Token ${this.$cookies.get('token')}`
                },
                data: {
                    first_name, last_name, email
                }
            })
            .then(res => {
                console.log(res.data)
                this.updateShow = false
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