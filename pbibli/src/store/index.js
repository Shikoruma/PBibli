import Vue from "vue";
import Vuex from "vuex";

import auth from "./auth.module";
import books from "./books.module";
import persons from "./persons.module";
import loans from "./loans.module";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    books,
    loans,
    persons,
  }
});
