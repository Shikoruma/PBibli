<template>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand :to="{ name: 'home' }" v-text="title"></b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav v-if="!isAuthenticated">
        <b-nav-item :to="{ name: 'home' }">Home</b-nav-item>
        <b-nav-item @click="login">Sign in</b-nav-item>
      </b-navbar-nav>
      <b-navbar-nav v-else>
        <b-nav-item :to="{ name: 'home' }">Home</b-nav-item>
        <b-nav-item >Loans</b-nav-item>
        <b-nav-item >Users</b-nav-item>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  import {TITLE} from "@/common/config";
  export default {
    name: "RwvHeader",
    data() {
      return {
          title:TITLE,
      }
    },

    computed: {
      ...mapGetters(["isAuthenticated"])
    },
    methods: {
      login() {
        window.location.replace("/admin/login/?next=/")
      }
    }
  };
</script>
