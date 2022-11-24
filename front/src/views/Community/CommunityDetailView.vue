<template>
  <div class="container" id="reviewdetail">
    <div v-show="!isUpdateOpen" class="container">
        <div class="row pt-5" id="reviewTitle">
            <h1>제목 : {{ reviewDetail?.title }}</h1>
        </div>
        <div class="row text-end p-3" id="reviewUser">
            <h2 @click="goToReviewer">작성자 : {{ reviewDetail?.user?.username }}</h2>
        </div>
        <div class="row">
            <div class="col">
                <MyCard
                    :movie="reviewMovieGet || reviewDetail.movie"
                    class="w-100"
                 />
            </div>
            <div class="col">
                <div class="row d-flex flex-column">
                    <div class="col">
                        <button 
                            @click="likeReview" 
                            v-show="$store.getters.userPkGetters && !reviewDetail?.like_users.includes($store.getters.userPkGetters) && $store.getters.userPkGetters !== reviewDetail.user.id"
                            class="btn"
                            id="likebtn"
                        >리뷰 좋아요</button>
                        <button 
                        @click="likeReview" 
                        v-show="$store.getters.userPkGetters && reviewDetail?.like_users.includes($store.getters.userPkGetters) && $store.getters.userPkGetters !== reviewDetail.user.id" class="btn" id="unlikebtn">리뷰 좋아요 취소</button>
                        <div class="row justify-content-evenly m-2">
                            <button @click="deleteReview" class="btn btn-danger col-4" v-show="$store.getters.userPkGetters === reviewDetail.user.id">리뷰 삭제</button>
                            <button @click="isUpdateOpen = !isUpdateOpen" class="btn btn-primary col-4" v-show="$store.getters.userPkGetters === reviewDetail.user.id">리뷰 수정</button>
                        </div>
                    </div>
                    <div class="col-9 h-100 w-100">
                        <h4>내용<br><br>{{ reviewDetail?.content }}</h4>
                    </div>
                    <div class="col-2 w-100">
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
                    
                </div>
            </div>
        </div>
        
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
import MyCard from '@/components/MyCard'

export default {
    name: 'CommunityDetailView',
    components: {
        CommunityComment,
        MyCard
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
                this.$store.commit('DELETE_REVIEW', this.reviewDetail.id)
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
        },
        goToReviewer() {
            this.$router.push({name: 'userinfo', params: { userPk: this.reviewDetail.user.id}})
        }
    },
    created() {
        this.$store.commit('REVIEW_NUMS_GET', this.$route.params.movieid)
        this.getReviewDetail()
    },
    computed: {
        reviewMovieGet() {
            return this.$store.getters.getReviewMovie
        }
    }
}
</script>

<style>
#reviewdetail {
    color: white;
}
#reviewTitle{
    background-color: rgb(47, 37, 25);
}
#reviewUser {
    background-color: rgb(74, 63, 53);
}
#likebtn {
    background-color: #FA7D09;
    animation: like 2s;
}
#unlikebtn {
    background-color: #FF4301;
    animation: like 2s;
}
</style>