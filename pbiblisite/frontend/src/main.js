import Vue from "vue";
import VueRouter from "vue-router";
import Vuex from "vuex";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import { CHECK_AUTH } from "./store/actions.type";
import ApiService from "./common/api.service";
ApiService.init();

//Ensure we checked auth before each page load.
router.beforeEach((to, from, next) => {
  if (to.name == "home") next();
  else return Promise.all([store.dispatch(CHECK_AUTH)]).then(next);
});

Vue.filter("field", function(value, field) {
  if (!value || !(field in value)) return "";
  return value[field];
});

Vue.use(VueRouter);
Vue.use(Vuex);

Vue.config.productionTip = false;
Vue.config.productionTip = true;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
