import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPageView from '@/views/MainPageView'
import SearchPageView from '@/views/SearchPageView'
import LoginPageView from '@/views/LoginPageView'
import SignupPageView from '@/views/SignupPageView'
import UserInfoPageView from '@/views/UserInfoPageView'

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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
