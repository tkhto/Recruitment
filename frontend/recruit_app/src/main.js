// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import settings from './settings.js'
import axios from 'axios'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import '../static/js/gt.js'
import mavonEditor from 'mavon-editor'
import 'mavon-editor/dist/css/index.css'
const moment = require('moment')
// use
Vue.use(mavonEditor)
new Vue({
    'el': '#main',
    data() {
        return { value: '' }
    }
})

Vue.config.productionTip = false

Vue.use(ElementUI)
Vue.prototype.settings = settings
Vue.prototype.axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  axios,
  components: { App },
  template: '<App/>'
})

// npm install mavon-editor --save