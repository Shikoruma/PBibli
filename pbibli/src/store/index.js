import Vue from "vue";
import Vuex from "vuex";

import auth from "./auth.module";
import books from "./books.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    books,
  }
});
