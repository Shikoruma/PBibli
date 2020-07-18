<template>
  <div v-if="loaded">
    <h1>Rechercher</h1>
    <div class="row">
      <div class="col-xl-3">
        <div class="card">
          <div class="card-header">
            <h4>Filtres</h4>
          </div>
          <div class="card-body">
            <form class="form">
              <div class="form-group">
                <label>Chercher</label
                ><input
                  type="search"
                  class="form-control"
                  placeholder="Titre, Autheur"
                  v-model="search_input"
                />
              </div>
            </form>
          </div>
        </div>
      </div>
      <div class="col">
        <div class="card">
          <div class="card-header">
            <form class="form form-inline">
              <div class="form-group">
                <label class="mr-1">Ordre : </label>
                <select class="form-control" v-model="sort_input">
                  <option
                    v-for="item in sort_choices"
                    :value="item.value"
                    :key="item.value"
                    >{{ item.label }}</option
                  >
                </select>
              </div>
            </form>

            <pagination
              :total-pages="pages_count"
              :total="objects_filtered.length"
              :per-page="10"
              :current-page="current_page"
              @pagechanged="onPageChange"
            />
          </div>
          <div class="card-body">
            <ul class="list-group list-group-flush">
              <li
                v-for="item in objects_paginated"
                :key="item.id"
                class="list-group-item list-group-item-action flex-column align-items-start"
              >
                <div class="d-flex w-100 justify-content-between">
                  <h4>{{ item.prettytitle }}</h4>
                  <strong>{{
                    userById(item.owner) | field("username")
                  }}</strong>
                </div>
                <p class=""><strong>Autheur:</strong> {{ item.author }}</p>
                <h6 v-if="item.abstract">Résumé</h6>
                <p class="">{{ item.abstract }}</p>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import Pagination from "@/components/Pagination";
export default {
  name: "Search",
  components: {
    Pagination
  },
  data() {
    return {
      loaded: false,
      search_input: "",
      sort_input: 1,
      type_input: 1,
      tags: [],
      current_page: 1,
      sort_choices: {
        title: { value: 1, label: "Titre" },
        author: { value: 2, label: "Autheur" }
      }
    };
  },
  computed: {
    ...mapGetters({
      allbooks: "books/allbooks",
      userById: "users/byId"
    }),
    objects_list() {
      return this.allbooks;
    },
    objects_filtered() {
      var filtered = this.objects_list.filter(item => {
        var filterstring = ["prettytitle", "author"].some(field => {
          if (item[field] == null) return false;
          return (
            item[field].toLowerCase().indexOf(this.search_input.toLowerCase()) >
            -1
          );
        });
        return filterstring;
      });
      return filtered.sort((a, b) => {
        if (this.sort_input == this.sort_choices.title.value)
          return a.prettytitle.localeCompare(b.prettytitle);
        if (this.sort_input == this.sort_choices.author.value)
          return a.author.localeCompare(b.author);
      });
    },
    objects_paginated() {
      return this.objects_filtered.slice(
        (this.current_page - 1) * process.env.VUE_APP_MAXLIST,
        this.current_page * process.env.VUE_APP_MAXLIST
      );
    },
    pages_count() {
      return Math.ceil(
        this.objects_filtered.length / process.env.VUE_APP_MAXLIST
      );
    }
  },
  methods: {
    onPageChange(page) {
      this.current_page = page;
    }
  },
  beforeMount() {
    var pall = [];
    pall.push(this.$store.dispatch("books/fetchAllBooks"));
    pall.push(this.$store.dispatch("users/fetchList"));
    Promise.all(pall).then(() => {
      this.loaded = true;
    });
  }
};
</script>
