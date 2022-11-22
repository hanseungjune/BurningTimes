<template>
  <div>
    ---{{ recommentThis.user.username }} {{ recommentThis.content}} 
        <button class="btn btn-primary" @click="updateRecommentOpen = !updateRecommentOpen">댓글수정</button>
        <button class="btn btn-danger" @click="deleteRecomment(recomment.review, recomment.id)">댓글삭제</button>
        <!-- 대댓글 수정폼 -->
        <form @submit.prevent="updateRecomment(recomment.review, recomment.id, updateRecommentInput)" v-show="updateRecommentOpen">
            <div class="form-floating m-3">
                <input type="text" class="form-control" id="updataRecommentInput" placeholder="대댓글수정" v-model.trim="updateRecommentInput">
                <label for="updataRecommentInput">대댓글수정</label>
            </div>
            <input class="btn btn-success" type="submit" value="대댓글수정">
        </form>
  </div>
</template>

<script>
export default {
    name: 'CommunityRecomment',
    data() {
        return {
            recommentThis : this.recomment,
            updateRecommentOpen: false,
            updateRecommentInput: this.recomment.content
        }
    },
    props: {
        recomment: Object,
    },
    methods: {
        deleteRecomment(reviewId, commentId) {
            this.$emit('deleteRecomment', reviewId, commentId)
        },
        updateRecomment(reviewId, commentId, content) {
            this.$emit('updateRecomment', reviewId, commentId, content)
            this.updateRecommentOpen = false
            this.recommentThis.content = content
        }
    }
}
</script>

<style>

</style>