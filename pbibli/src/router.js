import Vue from "vue";
import VueRouter from "vue-router";
import { CHECK_AUTH } from "./store/actions.type";
import store from './store'
import Books from "./views/Books"
import Persons from "./views/Persons"
import Loans from "./views/Loans"
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
        next({ name: "books" })
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
      name: "books",
      path: "/",
      component: Books,
    },
    {
      name: "persons",
      path: "/persons",
      component: Persons,
      beforeEnter : requireAuth,
    },
    {
      name: "loans",
      path: "/loans",
      component: Loans,
      beforeEnter : requireAuth,
    },

  ]
});
