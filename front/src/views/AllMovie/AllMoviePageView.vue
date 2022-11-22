<template>
  <div class="container-fluid">
    <div class="row">
        <h1>전체 영화 페이지</h1>
    </div>
    <div class="row">
        <OrderList />
        <div class="col-9 row">
            <MyCard
                v-for="movie in orderList"
                :key="movie.id"
                :movie=movie
            />
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
    computed: {
        orderList() {
            return this.$store.getters.orderMovieGetters
        }
    },
    created() {
        const payload = {
                genre: [],
                order: ''
            }
        this.$store.dispatch('startMovieOrder', payload)
    }
}
</script>

<style>

</style>