import Vue from 'vue'
import App from './App.vue'
import Landing from './Landing.vue'
import Header from './Header.vue'
import Footer from './Footer.vue'
import ProductList from './ProductList.vue'
import SideBar from './SideBar.vue'

Vue.component('landing', Landing);
Vue.component('vue-header', Header);
Vue.component('vue-footer', Footer);
Vue.component('productlist', ProductList);
Vue.component('sidebar', SideBar);

new Vue({
  el: '#app',
  render: h => h(App)
})
