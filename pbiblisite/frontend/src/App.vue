<template>
  <div id="app" class="container">
    <div v-if="loaded">
      <Header />
      <router-view />
      <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    </div>
  </div>
</template>

<script>
import "./assets/style.css";
import Header from "@/views/Header";
import { mapGetters } from "vuex";
import { CHECK_AUTH } from "./store/actions.type";

export default {
  name: "App",
  components: {
    Header
  },
  data() {
    return {
      loaded: false
    };
  },
  computed: {
    ...mapGetters(["authUser"])
  },
  mounted() {
    document.title = process.env.VUE_APP_TITLE;
    this.$store
      .dispatch(CHECK_AUTH)
      .then(() => {
        var pall = [];
        pall.push(
          import(
            /* webpackChunkName: "store-books" */ "@/store/books.module"
          ).then(module => {
            this.$store.registerModule("books", module.default);
          })
        );
        pall.push(
          import(
            /* webpackChunkName: "store-loans" */ "@/store/loans.module"
          ).then(module => {
            this.$store.registerModule("loans", module.default);
          })
        );
        pall.push(
          import(
            /* webpackChunkName: "store-users" */ "@/store/users.module"
          ).then(module => {
            this.$store.registerModule("users", module.default);
          })
        );

        Promise.all(pall).then(() => {
          this.loaded = true;
        });
      })
      .catch(() => {
        this.loaded = true;
      });
  }
};
</script>

<style>
@media only screen and (min-width: 1200px) {
  .container {
    max-width: 1500px;
  }
}
</style>
