import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import VueRouter from "vue-router";
import jwt_decode from 'jwt-decode'
import Vuex from 'vuex'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import App from './App.vue'
import router from './router'
import store from './store'

import {
    CHECK_AUTH
} from "./store/actions.type";
import ApiService from "./common/api.service";
import {
    errorValue,
    errorKey
} from "./common/error.filter";
ApiService.init();
Vue.filter("errorV", errorValue);
Vue.filter("errorK", errorKey);

//Ensure we checked auth before each page load.
router.beforeEach((to, from, next) => {
    return Promise.all([store.dispatch(CHECK_AUTH)])
        .then(next)
});

Vue.use(VueRouter);
Vue.use(BootstrapVue)
Vue.use(Vuex);

Vue.config.productionTip = false
Vue.config.productionTip = true 

new Vue({
        router,
        store,
        render: h => h(App)
    })
    .$mount('#app')
