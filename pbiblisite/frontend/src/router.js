import Vue from "vue";
import VueRouter from "vue-router";
import store from "./store";
import Home from "@/views/Home.vue";

Vue.use(VueRouter);

function requireAuth(to, from, next) {
  if (store.getters.isAuthenticated) {
    next();
  } else {
    next({ name: "home" });
  }
}

export default new VueRouter({
  routes: [
    {
      name: "home",
      path: "/",
      component: Home
    },
    {
      name: "search",
      path: "/search",
      component: () =>
        import(/* webpackChunkName: "search" */ "@/views/Search.vue")
    },
    {
      name: "profile",
      path: "/profile",
      component: () =>
        import(/* webpackChunkName: "profile" */ "@/views/Profile.vue"),
      beforeEnter: requireAuth
    },
    {
      path: "/books",
      component: () =>
        import(/* webpackChunkName: "book" */ "@/views/Books.vue"),
      beforeEnter: requireAuth,
      children: [
        {
          path: "",
          name: "books",
          component: () =>
            import(/* webpackChunkName: "booklist" */ "@/views/BooksList.vue")
        },
        {
          path: ":bookid",
          name: "book",
          meta: {
            routeparam: "bookid",
            routedelete: "books"
          },
          component: () =>
            import(/* webpackChunkName: "bookedit" */ "@/views/BookEdit.vue")
        }
      ]
    },
    {
      name: "loansin",
      path: "/loansin",
      component: () =>
        import(/* webpackChunkName: "loansin" */ "@/views/LoansIn.vue"),
      beforeEnter: requireAuth
    },
    {
      path: "/loansout",
      component: () =>
        import(/* webpackChunkName: "loansout" */ "@/views/LoansOut.vue"),
      beforeEnter: requireAuth,
      children: [
        {
          path: "",
          name: "loansout",
          component: () =>
            import(
              /* webpackChunkName: "loansoutlist" */ "@/views/LoansOutList.vue"
            )
        },
        {
          path: ":loanid",
          name: "loanout",
          meta: {
            routeparam: "loanid",
            routedelete: "loansout"
          },
          component: () =>
            import(
              /* webpackChunkName: "loanoutedit" */ "@/views/LoanOutEdit.vue"
            )
        }
      ]
    }
  ]
});
