<template>
  <div>
    <span @click="recommentOpen = !recommentOpen">{{ commentThis.user.username }} {{ commentThis.content}}</span>
    <button class="btn btn-danger" @click="deleteComment(commentThis.review, commentThis.id)">댓글삭제</button>
    <div v-for="recomment in commentThis.childcomment" :key="recomment.id">
        ---{{ recomment.user.username }} {{ recomment.content}} 
        <button class="btn btn-danger" @click="deleteReComment(recomment.review, recomment.id)">댓글삭제</button></div>
    <form @submit.prevent="createRecomment" v-show="recommentOpen">
        <div class="form-floating m-3">
            <input type="text" class="form-control" id="recommentInput" placeholder="대댓글" v-model.trim="recommentInput">
            <label for="recommentInput">대댓글</label>
        </div>
        <input class="btn btn-success" type="submit" value="대댓글작성">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityComment',
    data() {
        return {
            recommentOpen: false,
            recommentInput: null,
            commentThis: this.comment
        }
    },
    props: {
        comment: Object,
    },
    methods: {
        createRecomment() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.comment.review
            const content = this.recommentInput
            const user = this.$store.getters.userPkGetters
            const parent = this.comment.id
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/`,
                data: {
                    content, user, parent
                },
            })
            .then(res => {
                console.log(res.data)
                this.commentThis.childcomment.push(res.data)
                this.recommentInput = null
                this.recommentOpen = false
            })
            .catch(err => console.log(err))
        },
        deleteComment(reviewId, commentId) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
            })
            .then(res => {
                console.log(res.data)
                this.$emit('deleteComment', commentId)
            })
            .catch(err => console.log(err))
        },
        deleteReComment(reviewId, commentId) {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = reviewId
            const commentid = commentId
            axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/${commentid}/`,
            })
            .then(res => {
                console.log(res.data)
                this.commentThis.childcomment = this.commentThis.childcomment.filter(el => {
                    if (el.id !== commentId) {
                        return el
                    }
                })
            })
            .catch(err => console.log(err))
        }
    }
}
</script>

<style>

</style>