import Vue from "vue";
import createCrud from "@/common/storeCrudHelper";

import ApiService from "@/common/api.service";

const books_extra = {
  state: {
    temp: null,
    allbooks: {},
    listallbooks: {}
  },
  getters: {
    temp(state) {
      return state.temp;
    },
    allbooks(state) {
      return state.listallbooks.map(id => state.allbooks[id.toString()]);
    },
    allById(state) {
      return id => (id ? state.allbooks[id.toString()] : null);
    }
  },
  actions: {
    findByISBN(context, isbn) {
      return ApiService.post("books/find_book", { isbn: isbn }).then(
        ({ data }) => {
          return data;
        }
      );
    },
    fetchAllBooks({ commit }) {
      return ApiService.query("allbooks").then(({ data }) => {
        commit("setAllBooks", data);
        return data;
      });
    }
  },
  mutations: {
    setTemp(state, data) {
      state.temp = data;
    },
    setAllBooks(state, data) {
      data.forEach(m => {
        Vue.set(state.allbooks, m["id"].toString(), m);
      });
      state.listallbooks = data.map(m => m["id"].toString());
    }
  }
};
const books = createCrud("books", books_extra);
export default books;
