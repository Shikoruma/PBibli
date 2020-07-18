<template>
  <div class="row">
    <div class="col-12 col-md-6">
      <div class="card">
        <div class="card-header">
          <input v-model="search_input" type="search" placeholder="Search" />
          <div class="btn-group float-right" role="group">
            <router-link
              class="btn btn-primary"
              role="button"
              :to="{ name: 'book', params: { bookid: 'new' } }"
              >Ajouter</router-link
            >
          </div>
        </div>
        <div class="card-body">
          <div class="table-responsive table-hover">
            <table class="table">
              <thead>
                <tr>
                  <th>Titre</th>
                </tr>
              </thead>
              <tbody>
                <tr
                  v-for="item in objects_paginated"
                  :key="item.id"
                  v-on:click="selected_object = item"
                >
                  <td v-text="item.prettytitle"></td>
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
          <h3 class="float-left" v-text="selected_object.prettytitle"></h3>
          <div class="btn-group float-right" role="group">
            <router-link
              class="btn btn-primary"
              role="button"
              :to="{
                name: 'book',
                params: { bookid: selected_object.id }
              }"
              >Modifier</router-link
            >
            <router-link
              class="btn btn-primary"
              role="button"
              :to="{
                name: 'loanout',
                params: { loanid: 'new' },
                query: { bookid: selected_object.id }
              }"
              >Prêter</router-link
            >
          </div>
        </div>
        <div class="card-body">
          <table class="table">
            <tr>
              <th scope="row">ISBN</th>
              <td>{{ selected_object.isbn }}</td>
            </tr>
            <tr>
              <th scope="row">Titre</th>
              <td>{{ selected_object.title }}</td>
            </tr>
            <tr>
              <th scope="row">Author</th>
              <td>{{ selected_object.author }}</td>
            </tr>
            <tr>
              <th scope="row">Titre série</th>
              <td>{{ selected_object.serie_title }}</td>
            </tr>
            <tr>
              <th scope="row">Numéro tome</th>
              <td>{{ selected_object.num_volume }}</td>
            </tr>
            <tr>
              <th scope="row">Dématérialisé</th>
              <td>{{ selected_object.demat ? "oui" : "non" }}</td>
            </tr>
            <tr>
              <th scope="row">Localisation</th>
              <td>{{ selected_object.localisation }}</td>
            </tr>
          </table>

          <p class="card-text">
            {{ selected_object.abstract }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { ListMixin } from "@/common/mixins";
export default {
  name: "BookList",
  mixins: [ListMixin],
  data() {
    return {
      search_fields: ["title", "serie_title", "author", "isbn"],
      ressource: "books"
    };
  },
  computed: {
    ...mapGetters(["authUser"])
  },
  methods: {}
};
</script>
