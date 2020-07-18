<template>
  <div class="row" v-if="loaded">
    <h1 class="col-12">Mes emprunts</h1>
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
                  <th>Propriétaire</th>
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
                  <td>
                    {{
                      userById(bookById(item.book).owner) | field("username")
                    }}
                  </td>
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
          <div class="btn-group float-right" role="group"></div>
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
              <th scope="row">Propriétaire</th>
              <td>
                {{
                  userById(bookById(selected_object.book).owner)
                    | field("username")
                }}
              </td>
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
  name: "LoansOUtList",
  mixins: [ListMixin],
  computed: {
    ...mapGetters({
      bookById: "books/allById",
      userById: "users/byId",
      authUser: "authUser"
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
      pall.push(this.$store.dispatch("books/fetchAllBooks"));
      return Promise.all(pall).then(() => {
        this.loaded = true;
      });
    },
    search_fields(list, searchinput) {
      var silc = searchinput.toLowerCase();
      return list
        .filter(item => {
          if (!item.borrower) return false;

          var bookname = this.bookById(item.book)
            .prettytitle.toLowerCase()
            .includes(silc);
          return (
            item.borrower == this.authUser.id &&
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
