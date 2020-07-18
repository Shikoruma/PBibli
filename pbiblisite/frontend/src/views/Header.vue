<template>
  <nav class="navbar navbar-light navbar-expand-md">
    <div class="container-fluid">
      <a class="navbar-brand" href="/"
        ><strong>{{ title }}</strong></a
      >
      <button
        data-toggle="collapse"
        class="navbar-toggler"
        data-target="#navcol-1"
      >
        <span class="sr-only">Toggle navigation</span
        ><span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navcol-1">
        <ul class="nav navbar-nav mr-auto">
          <router-link
            v-if="isAuthenticated"
            active-class="active"
            exact
            :to="{ name: 'search' }"
            v-slot="{ href, route, navigate }"
          >
            <li class="nav-item" role="presentation">
              <a class="nav-link" :href="href" @click="navigate">Rechercher</a>
            </li>
          </router-link>
        </ul>
        <ul v-if="isAuthenticated" class="nav navbar-nav">
          <li class="nav-item" role="presentation">
            <Dropdown
              :items="userroutes"
              :label="authUser.username"
              classtoogle="nav-link"
            />
          </li>

          <li class="nav-item" role="presentation">
            <a class="nav-link" href="#" @click="logout">Logout </a>
          </li>
        </ul>
        <ul v-else class="nav navbar-nav">
          <li class="nav-item" role="presentation">
            <a class="nav-link" href="/auth/login">Login</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
import { mapGetters } from "vuex";
import Dropdown from "@/components/Dropdown";
export default {
  name: "Header",
  components: {
    Dropdown
  },
  data() {
    return {
      title: process.env.VUE_APP_TITLE,
      cas: process.env.VUE_APP_CASNAME,
      userroutes: [
        {
          to: { name: "profile" },
          label: "Profile"
        },
        {
          to: { name: "books" },
          label: "Mes livres"
        },
        {
          to: { name: "loansout" },
          label: "Mes prêts"
        },
        {
          to: { name: "loansin" },
          label: "Mes emprumts"
        }
      ]
    };
  },

  computed: {
    ...mapGetters(["authUser", "isAuthenticated", "isAdmin"])
  },
  methods: {
    logout(e) {
      e.preventDefault();
      window.location = "/auth/logout";
    }
  }
};
</script>
