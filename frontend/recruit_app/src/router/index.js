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
import Manage from '@/components/Manage'
import Change from '@/components/Common/Change'
import Join from '@/components/Manage/Join'
import CreatePosition from '@/components/Manage/Position/CreatePosition'
import EditPosition from '@/components/Manage/Position/EditPosition'
import Delivery from '@/components/Profile/Resume/Delivery'
import Received from '@/components/Manage/Received'

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
          path: '/delivery',
          component: Delivery
        },
        {
          path: '/received',
          component: Received
        },
        {
          path: '/manage',
          component: Manage
        },
        {
          path: '/change',
          component: Change
        },
        {
          path: '/createposition/:id',
          component: CreatePosition
        },
        {
          path: '/editposition/:id',
          component: EditPosition
        },
        {
          path: '/manage/join',
          component: Join
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
