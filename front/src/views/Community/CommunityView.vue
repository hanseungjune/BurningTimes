<template>
  <div class="container d-flex flex-column justify-content-center">
    <div class="row justify-content-between">
        <span class="col-3">리뷰 페이지</span>
        <router-link class="btn btn-success col-2" :to="{ name: 'communitycreate'}">리뷰 작성</router-link>
    </div>
    <div class="container justfy-content-center">
        <table class="table table-hover">
            <thead>
                <tr>
                <th scope="col" id="rNum">번호</th>
                <th scope="col" id="rmovie">영화</th>
                <th scope="col" id="rtitle">제목</th>
                <th scope="col" id="rRecommend">추천수</th>
                <th scope="col" id="rWriter">작성자</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                    v-for="review in communityList"
                    :key="review.id"
                    @click="moveToDetail(review.id, review.movie.id)"
                >
                <td scope="col" id="rNum">{{ review.id }}</td>
                <td scope="col" id="rmovie">{{ review.movie.title.slice(0, 12) + '...' }}</td>
                <td scope="col" id="rtitle">{{ review.title }}</td>
                <td scope="col" id="rRecommend">{{ review.like_users.length }}</td>
                <td scope="col" id="rWriter">{{ review.user.username }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    {{ pageRange }}
    <nav aria-label="Page navigation example">
                <ul class="pagination justify-content-center mt-5">
                    <!-- 처음으로 -->
                    <li class="page-item">
                    <a class="page-link" @click.prevent="presentPage = 1"><i class="bi bi-chevron-double-left"></i></a>
                    </li>
                    <!-- 뒤로 -->
                    <li class="page-item ">
                    <a class="page-link" @click.prevent="pMinus"><i class="bi bi-chevron-left" style="all: unset;"></i></a>
                    </li>
                    <!-- ... -->
                    <li class="page-item disabled" v-show="presentFirstPage !== 1">
                    <a class="page-link"><i class="bi bi-three-dots"></i></a>
                    </li>
                    <!-- 시작 -->
                    <li 
                        v-for="(n, index) in pageRange"
                        :key=index
                        class="page-item"
                        :class="{ 'active' : n === presentPage }"
                        @click.prevent="presentPage=n"
                    >
                        <a class="page-link" href="#">{{ n }}</a>
                    </li>
                    <!-- 끝 -->
                    <li class="page-item disabled" v-show="orderListmaxPage !== presentLastPage">
                    <a class="page-link"><i class="bi bi-three-dots"></i></a>
                    </li>
                    <!-- 앞으로 -->
                    <li class="page-item">
                    <a class="page-link" href="#" @click.prevent="pPlus"><i class="bi bi-chevron-right" style="all: unset;"></i></a>
                    </li>
                    <!-- 끝으로 -->
                    <li class="page-item" @click.prevent="presentPage = orderListmaxPage">
                    <a class="page-link" href="#"><i class="bi bi-chevron-double-right"></i></a>
                    </li>
                </ul>
            </nav>
  </div>
<!-- <div 
        v-for="review in communityList"
        :key="review.id"
     >
        {{ review.id }} {{ review.movie.title }} {{review.title}} {{ review.user.username }} {{ review.created_at.slice(0,10)}}
        <button class="btn btn-primary" @click="moveToDetail(review.id, review.movie.id)">상세</button>
        <br>
        <br>
    </div> -->
</template>

<script>
import axios from 'axios'

export default {
    name: 'CommunityView',
    data() {
        return{
            communityList: null,
            presentPage: 1,
            pageRange: []
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
        },
        pMinus() {
            if (this.presentPage > 2) {
                this.presentPage -= 1
            }
        },
        pPlus() {
            if (this.presentPage < this.orderListmaxPage) {
                this.presentPage += 1
            }
        }
    },
    computed: {
        orderListmaxPage() {
            console.log(Math.ceil(this.communityList.length/8))
            return Math.ceil(this.communityList.length/8)
        },
        presentFirstPage() {
            if (this.presentPage - 2 < 1) {
                return 1
            } else {
                return this.presentPage -2 
            }
        },
        presentLastPage() {
            if (this.presentFirstPage + 4 < this.orderListmaxPage) {
                return this.presentFirstPage + 4
            } else {
                return this.orderListmaxPage
            }
        },
    },
    created() {
        this.getCommunityList()
        for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
                this.pageRange.push(i)
        }
    }
}


</script>

<style>
#rNum {
    width: 10vw;
}
#rmovie {
    width: 20vw
}
#rtitle {
    width: 50vw;
}
#rRecommend {
    width: 10vw;
}
#rWriter {
    width: 10vw;
}
</style>