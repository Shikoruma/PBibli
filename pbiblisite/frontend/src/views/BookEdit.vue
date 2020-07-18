<template>
  <div class="row">
    <div class="col-12">
      <div class="card" v-if="object">
        <div class="card-header">
          <h3 class="float-left" v-text="cardName"></h3>
          <div class="btn-group float-right" role="group">
            <router-link
              class="btn btn-primary"
              role="button"
              :to="{ name: 'books' }"
              >Retour</router-link
            ><router-link
              class="btn btn-warning"
              role="button"
              :to="{
                name: 'loanout',
                params: { loanid: 'new' },
                query: { bookid: object.id }
              }"
              >Prêter</router-link
            >
          </div>
        </div>
        <div class="card-body">
          <form id="editor-form">
            <div class="form-row">
              <div class="col">
                <div class="form-group">
                  <label>ISBN</label>
                  <div class="input-group mb-3">
                    <input
                      v-model="object.isbn"
                      class="form-control"
                      type="text"
                      v-on:keyup.enter="findByISBN"
                      required
                    />
                    <div class="input-group-append" v-if="is_new">
                      <button
                        class="btn btn-outline-primary"
                        :class="{
                          'btn-outline-primary': !searching,
                          'btn-outline-warning': searching
                        }"
                        type="button"
                        @click="findByISBN"
                        :disabled="searching"
                      >
                        {{ !searching ? "Chercher" : "En cours" }}
                      </button>
                    </div>
                  </div>
                </div>
                <div class="form-group">
                  <label>Titre</label
                  ><input
                    v-model="object.title"
                    class="form-control"
                    type="text"
                    required
                  />
                </div>
                <div class="form-group">
                  <label>Autheur</label
                  ><input
                    v-model="object.author"
                    class="form-control"
                    type="text"
                    required
                  />
                </div>
                <div class="form-group">
                  <label>Titre série</label
                  ><input
                    v-model="object.serie_title"
                    class="form-control"
                    type="text"
                  />
                </div>
                <div class="form-group">
                  <label>Numéro Tome</label
                  ><input
                    v-model="object.num_volume"
                    class="form-control"
                    type="text"
                  />
                </div>
                <div class="form-group">
                  <label>Localisation</label
                  ><input
                    v-model="object.localisation"
                    class="form-control"
                    type="text"
                  />
                </div>
                <div class="form-group">
                  <label>Démat</label
                  ><input
                    v-model="object.demat"
                    class="form-control"
                    type="checkbox"
                  />
                </div>
                <div class="form-group">
                  <label>Résumé</label
                  ><textarea v-model="object.abstract" class="form-control" />
                </div>
              </div>
            </div>
            <div class="btn-group" role="group">
              <button
                v-if="is_new"
                class="btn btn-primary"
                type="button"
                v-on:click="create"
              >
                Ajouter
              </button>
              <button
                v-if="!is_new"
                class="btn btn-primary"
                type="button"
                v-on:click="update"
              >
                Modifier
              </button>
              <button
                v-if="!is_new && object.serie_title"
                class="btn btn-primary"
                type="button"
                v-on:click="addVolume"
              >
                Ajouter un tome
              </button>

              <button
                v-if="!is_new"
                class="btn btn-danger"
                type="button"
                v-on:click="destroy"
              >
                Supprimer
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { EditMixin } from "@/common/mixins";
// @ is an alias to /src
export default {
  name: "BookEdit",
  mixins: [EditMixin],
  data() {
    return {
      ressource: "books",
      new_label: "Nouveau Livre",
      object_name: "Livre",
      searching: false
    };
  },
  computed: {},
  methods: {
    get_empty() {
      var temp = this.$store.getters["books/temp"];
      if (temp) {
        this.$store.commit("books/setTemp", null);
        return temp;
      }
      return {
        title: "",
        author: "",
        isbn: ""
      };
    },
    make_label() {
      return this.object.prettytitle;
    },
    addVolume() {
      this.$store.commit("books/setTemp", {
        serie_title: this.object.serie_title,
        author: this.object.author,
        num_volume: this.object.num_volume + 1,
        localisation: this.object.localisation,
        demat: this.object.demat
      });
      this.$router.push({ name: "book", params: { bookid: "new" } });
    },
    findByISBN() {
      if (this.is_new) {
        this.searching = true;
        this.$store
          .dispatch("books/findByISBN", this.object.isbn)
          .then(data => {
            this.object = Object.assign({}, data);
            this.searching = false;
          })
          .catch(e => {
            console.log(e.response);
            this.searching = false;
          });
      }
    }
  }
};
</script>
