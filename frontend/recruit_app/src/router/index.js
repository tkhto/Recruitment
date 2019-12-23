import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index.vue'
import Home from '@/components/Home'
import Profile from '@/components/Profile'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/home',
    },
    {
      path: '/home',
      component: Index,
      children: [
        {
          path: '',
          component: Home
        },
        {
          path: '/profile',
          component: Profile
        }
      ]
    }
  ]
})
