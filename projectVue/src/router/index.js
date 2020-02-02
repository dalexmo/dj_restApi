import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import productosList from '@/components/productos/productosList'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/productos',
      name: 'ProductosList',
      component: productosList
    }
  ],
  mode: 'history'
})
