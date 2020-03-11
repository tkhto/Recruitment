import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/index.vue'
import Home from '@/components/Home'
import Profile from '@/components/Profile'
import Comdetail from '@/components/Comdetail'
import Posdetail from '@/components/Posdetail'
import Positions from '@/components/Positions'
import Companys from '@/components/Companys'
import Resume from '@/components/Profile/Resume'
import CreateResume from '@/components/Profile/CreateResume'
import EditResume from '@/components/Profile/EditResume'
import CreateArticle from '@/components/Profile/CreateArticle'
import EditArticle from '@/components/Profile/EditArticle'
import Article from '@/components/Profile/Article'

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
        },
        {
          path: '/company/:id',
          component: Comdetail
        },
        {
          path: '/position/:id',
          component: Posdetail
        },
        {
          path: '/positions',
          component: Positions
        },
        {
          path: '/companys',
          component: Companys
        },
        {
          path: '/createarticle/:id',
          component: CreateArticle
        },
        {
          path: '/article/:id',
          component: Article
        },
        {
          path: '/editarticle/:id',
          component: EditArticle
        },
        {
          path: '/resume/:id',
          component: Resume
        },
        {
          path: '/createresume/:id',
          component: CreateResume
        },
        {
          path: '/editresume/:id',
          component: EditResume
        }
      ]
    }
  ]
})
