<template>
  <div class="container">
    <div v-show="!isUpdateOpen">
        <h1>제목 : {{ reviewDetail?.title }}</h1>
        <h2>작성자 : {{ reviewDetail?.user?.username }}</h2>
        <h3>영화 : {{ reviewDetail?.movie?.title }}</h3>
        <button @click="likeReview" v-show="!reviewDetail?.like_users.includes($store.getters.userPkGetters)">리뷰 좋아요</button>
        <button @click="likeReview" v-show="reviewDetail?.like_users.includes($store.getters.userPkGetters)">리뷰 좋아요 취소</button>
        <div>
            <button @click="deleteReview" class="btn btn-danger">리뷰 삭제</button>
            <button @click="isUpdateOpen = !isUpdateOpen" class="btn btn-primary">리뷰 수정</button>
        </div>
        <img :src="'https://image.tmdb.org/t/p/w500/'+ reviewDetail?.movie.poster_path" alt="">
        <h4>내용 : {{ reviewDetail?.content }}</h4>
        <CommunityComment 
            v-for="comment in reviewDetail?.comments.filter(el => {
                if (!el.parent_comment) {
                    return el
                }
            })" 
            :key="comment.id"
            :comment = comment
            @deleteComment="deleteComment"
        />
        <form @submit.prevent="createComment">
        <div class="form-floating m-3">
            <textarea class="form-control" placeholder="내용을 작성하세요" id="commentInput" style="height: 150px" v-model.trim="commentInput"></textarea>
            <label for="commentInput">Comment</label>
        </div>
        <input class="btn btn-success" type="submit" value="댓글작성">
        </form>
    </div>
    <!-- 수정페이지 -->
    <div v-show="isUpdateOpen">
        <h1>리뷰 수정입니다.</h1>
        <form @submit.prevent="updateReview">
        <div class="form-floating mb-3">
            <input type="text" class="form-control" id="titleInput" placeholder="게시글 제목" v-model.trim="reviewDetail.title">
            <label for="titleInput">Title</label>
        </div>
        영화를 하단에서 "꼭" 클릭해주세요!
        <div class="form-floating mb-3">
            <input type="text" class="form-control dropdown-toggle" id="titleInput" placeholder="영화" data-bs-toggle="dropdown" aria-expanded="false" v-model.trim="reviewDetail.movie.title" @input="seachMovie(reviewDetail.movie.title)">
            <label for="titleInput">Movie</label>
            <ul class="dropdown-menu dropdown-menu-dark w-100" aria-labelledby="dropdownMenuButton2">
            <li 
                v-for="movie in movieSelect"
                :key="movie.id"
            >
                <a class="dropdown-item" @click.prevent="titleGo(movie)">{{ movie?.title }}</a>
            </li>
            </ul>
        </div>
        <div class="form-floating mb-3">
            <textarea class="form-control" placeholder="내용을 작성하세요" id="contentInput" style="height: 400px" v-model.trim="reviewDetail.content"></textarea>
            <label for="contentInput">Content</label>
        </div>
        <input type="submit" class="btn btn-success" value="리뷰 수정!">
        </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CommunityComment from '@/components/Community/CommunityComment'

export default {
    name: 'CommunityDetailView',
    components: {
        CommunityComment,
    },
    data() {
        return {
            reviewDetail: null,
            updateMovieId: null,
            commentInput: null,
            isUpdateOpen: false,
            movieSelect: this.$store.getters.getAllMovies.slice(0, 5),
        }
    },
    methods: {
        // 리뷰 불러오기
        getReviewDetail() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.$route.params.reviewid
            const movieid = this.$route.params.movieid
            console.log(movieid, reviewid)
            return axios({
                method: 'get',
                url: `${DJANGO_API_URL}/api/v1/community/movie/${movieid}/review/${reviewid}/`,
            })
            .then(res => {
                this.reviewDetail = res.data
            })
            .catch(err => console.log(err))
        },
        // 리뷰 좋아요
        likeReview() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.reviewDetail.id
            const movieid = this.reviewDetail.movie.id
            const user = this.$store.getters.userPkGetters
            return axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/community/movie/${movieid}/review/${reviewid}/review_recommended/${user}/`,
            })
            .then(res => {
                console.log(res.data)
                if (this.reviewDetail.like_users.includes(user)) {
                    this.reviewDetail.like_users = this.reviewDetail.like_users.filter(el => {
                        if (el !== user) {
                            return el
                        }
                    })
                } else {
                    this.reviewDetail.like_users.push(user)
                }
            })
            .catch(err => console.log(err))
        },
        // 리뷰삭제
        deleteReview() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.reviewDetail.id
            const movieid = this.reviewDetail.movie.id
            console.log(movieid, reviewid)
            return axios({
                method: 'delete',
                url: `${DJANGO_API_URL}/api/v1/community/movie/${movieid}/review/${reviewid}/`,
            })
            .then(res => {
                console.log(res.data)
                this.$router.push({name: 'community'})
            })
            .catch(err => console.log(err))
        },
        // 코멘트 생성
        createComment() {
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            const reviewid = this.reviewDetail.id
            const content = this.commentInput
            const user = this.$store.getters.userPkGetters
            const parent = null
            axios({
                method: 'post',
                url: `${DJANGO_API_URL}/api/v1/community/review/${reviewid}/comments/`,
                data: {
                    content, user, parent
                },
            })
            .then(res => {
                this.reviewDetail = res.data
                this.commentInput = null
            })
            .then(() => {
                this.getReviewDetail()
            })
            .catch(err => console.log(err))
        },
        // 코멘트삭제
        deleteComment(commentid) {
            this.reviewDetail.comments = this.reviewDetail.comments.filter(el=>{
                if (el.id !== commentid) {
                    return el
                }
            })
        },
        // 수정에 쓸 함수
        // 영화검색 차용
        seachMovie(title) {
            const mlist = this.$store.getters.getAllMovies.filter(el => {
            if (el.title.includes(title)) {
                return el
            }
            })
            this.movieSelect = mlist.slice(0, 5)
        },
        titleGo(movie) {
            this.reviewDetail.movie.title = movie.title
            this.reviewDetail.movie.id = movie.id
        },
        updateReview() {
            const title = this.reviewDetail.title
            const content = this.reviewDetail.content
            const movieId = this.reviewDetail.movie.id
            const reviewId = this.reviewDetail.id
            const user = this.$store.getters.userPkGetters
            const DJANGO_API_URL = 'http://127.0.0.1:8000'
            return axios({
                method: 'put',
                url: `${DJANGO_API_URL}/api/v1/community/movie/${movieId}/review/${reviewId}/`,
                data: {
                    title, content, user
                }
            })
            .then(res => {
                this.reviewDetail = res.data
                this.isUpdateOpen = false
            })
            .catch(err => console.log(err))
        }
    },
    created() {
        this.getReviewDetail()
    }
}
</script>

<style>

</style>