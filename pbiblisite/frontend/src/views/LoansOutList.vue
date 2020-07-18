<template>
  <div class="row" v-if="loaded">
    <div class="col-12 col-md-6">
      <div class="card">
        <div class="card-header">
          <input v-model="search_input" type="search" placeholder="Search" />
          <div class="btn-group float-right" role="group"></div>
        </div>
        <div class="card-body">
          <div class="table-responsive table-hover">
            <table class="table">
              <thead>
                <tr>
                  <th>Titre</th>
                  <th>Emprunteur</th>
                  <th>Date retour prévue</th>
                  <th>Date retour</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="item in objects_paginated"
                  :key="item.id"
                  v-on:click="selected_object = item"
                >
                  <td>{{ bookById(item.book) | field("prettytitle") }}</td>
                  <td>{{ item.borrowername }}</td>
                  <td>{{ item.due_date }}</td>
                  <td>{{ item.return_date }}</td>
                </tr>
              </tbody>
            </table>
          </div>
          <pagination
            :total-pages="pages_count"
            :total="objects_filtered.length"
            :per-page="10"
            :current-page="current_page"
            @pagechanged="onPageChange"
          />
        </div>
      </div>
    </div>
    <div class="col-12 col-md-6">
      <div class="card" v-if="selected_object">
        <div class="card-header">
          <h3 class="float-left">
            {{ bookById(selected_object.book) | field("prettytitle") }}
            {{ selected_object.borrowername }}
          </h3>
          <div class="btn-group float-right" role="group">
            <router-link
              class="btn btn-primary"
              role="button"
              :to="{
                name: 'loanout',
                params: { loanid: selected_object.id }
              }"
              >Modifier</router-link
            >
          </div>
        </div>
        <div class="card-body">
          <table class="table">
            <tr>
              <th scope="row">Livre</th>
              <td>
                {{ bookById(selected_object.book) | field("prettytitle") }}
              </td>
            </tr>
            <tr>
              <th scope="row">Emprunteur</th>
              <td>{{ selected_object.borrowername }}</td>
            </tr>
            <tr>
              <th scope="row">Date sortie</th>
              <td>{{ selected_object.checkout_date }}</td>
            </tr>
            <tr>
              <th scope="row">Date retour prévue</th>
              <td>{{ selected_object.due_date }}</td>
            </tr>
            <tr>
              <th scope="row">Date retour</th>
              <td>{{ selected_object.return_date }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { ListMixin } from "@/common/mixins";
export default {
  name: "LoansOutList",
  mixins: [ListMixin],
  computed: {
    ...mapGetters({
      bookById: "books/byId",
      userById: "users/byId"
    })
  },
  data() {
    return {
      ressource: "loans",
      loaded: false,
      inprogress: false
    };
  },
  methods: {
    initComponent() {
      var pall = [];
      pall.push(this.$store.dispatch("users/fetchList"));
      pall.push(this.$store.dispatch("books/fetchList"));
      return Promise.all(pall).then(() => {
        this.loaded = true;
      });
    },
    search_fields(list, searchinput) {
      var silc = searchinput.toLowerCase();
      return list
        .filter(item => {
          var book = this.bookById(item.book);
          var bookname = false;
          if (book) {
            bookname = book.prettytitle.toLowerCase().includes(silc);
          } else return false;
          return (
            (bookname || item.borrowername.toLowerCase().includes(silc)) &&
            (!this.inprogress || item.return_date == null)
          );
        })
        .sort((a, b) => {
          return a.due_date.localeCompare(b.due_date);
        });
    }
  }
};
</script>
