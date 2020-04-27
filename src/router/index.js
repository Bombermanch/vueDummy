import Vue from 'vue';
import VueRouter from 'vue-router';
import Fetch from '../components/Fetch.vue';

Vue.use(VueRouter);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/fetch', 
      name: 'fetch',
      component: Fetch,
    }
  ],
});


