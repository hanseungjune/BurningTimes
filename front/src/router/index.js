import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/Main/MainPageView'
import SearchPageView from '@/views/Search/SearchPageView'
import LoginPageView from '@/views/User/LoginPageView'
import SignupPageView from '@/views/User/SignupPageView'
import UserInfoPageView from '@/views/User/UserInfoPageView'
import GenrePageView from '@/views/Genre/GenrePageView'
import MyTest from '@/views/MyTest'
import FirstSelectMovieView from '@/views/User/FirstSelectMovieView'
import CommunityView from '@/views/Community/CommunityView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'main',
    component: MainPageView
  },
  {
    path: '/search/:keyword',
    name: 'search',
    component: SearchPageView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupPageView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPageView
  },
  {
    path: '/userinfo/:userPk',
    name: 'userinfo',
    component: UserInfoPageView
  },
  {
    path: '/genre',
    name: 'genre',
    component: GenrePageView
  },
  {
    path: '/firstselect',
    name: 'firstselect',
    component: FirstSelectMovieView
  },
  {
    path: '/community',
    name: 'community',
    component: CommunityView
  },
  {
    path: '/test',
    name: 'test',
    component: MyTest
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
