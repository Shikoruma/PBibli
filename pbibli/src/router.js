import Vue from "vue";
import VueRouter from "vue-router";
import { CHECK_AUTH } from "./store/actions.type";
import store from './store'
import Books from "./views/Books"
import Login from "./views/Login"

Vue.use(VueRouter);

function requireAuth(to, from, next)
{
    if(store.getters.isAuthenticated)
    {
        next()
    }
    else
    {
        next({ name: "login" })
    }
}
function requireAdmin(to, from, next)
{
    if(store.getters.isAuthenticated && store.getters.isAdmin)
    {
        next()
    }
    else
    {
        next({ name: "home" })
    }
}

export default new VueRouter({
  routes: [
    {
      name: "home",
      path: "/",
      component: Books,
    },
    {
      name: "books",
      path: "/books",
      component: Books,
    },

  ]
});
