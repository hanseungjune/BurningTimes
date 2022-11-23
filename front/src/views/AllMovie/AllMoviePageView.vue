<template>
  <div class="container-fluid">
    <div class="row">
        <h1>All Movie!</h1>
    </div>
    <div class="row">
        <OrderList />
        <div class="col-9 row">
            <MyCard
                v-for="movie in orderList"
                :key="movie.id"
                :movie=movie
            />
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
    </div>
  </div>
</template>

<script>
import OrderList from '@/components/OrderList'
import MyCard from '@/components/MyCard'

export default {
    name: 'AllMoviePageView',
    components: {
        OrderList,
        MyCard
    },
    data() {
        return {
            presentPage: 1,
            pageRange: []
        }
    },
    methods: {
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
        orderList() {
            return this.$store.getters.orderMovieGetters
        },
        orderListmaxPage() {
            return parseInt(this.$store.getters.orderAllMovieGetters.length/8)
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
        const payload = {
                genre: [],
                order: ''
            }
        this.$store.dispatch('startMovieOrder', payload)
        for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
                this.pageRange.push(i)
            }
    },
    watch: {
        presentPage(value) {
            this.pageRange = []
            for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
                this.pageRange.push(i)
            }
            this.$store.commit('pageMove', value)
        },
        orderListmaxPage() {
            this.presentPage = 1,
            this.pageRange = []
            for(let i = this.presentFirstPage; i<=this.presentLastPage ; i++) {
                this.pageRange.push(i)
            }
        }
    }
}
</script>

<style>

</style>