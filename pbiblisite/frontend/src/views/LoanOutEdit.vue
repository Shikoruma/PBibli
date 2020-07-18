<template>
  <div class="row">
    <div class="col-12">
      <div class="card" v-if="object">
        <div class="card-header">
          <h3 v-text="cardName"></h3>
        </div>
        <div class="card-body">
          <form id="editor-form">
            <div class="form-row">
              <div class="col">
                <div class="form-group">
                  <label>Livre</label
                  ><input-datalist
                    v-model="object.book"
                    ressource="books"
                    :makeLabel="makeBookLabel"
                  ></input-datalist>
                </div>
                <div class="form-group">
                  <label>Emprunteur</label
                  ><input-datalist
                    v-model="object.borrower"
                    ressource="users"
                    :makeLabel="makeUserLabel"
                  ></input-datalist>
                </div>
                <div class="form-group">
                  <label>Nom Emprunteur</label
                  ><input
                    v-model="object.borrowerext"
                    class="form-control"
                    type="text"
                  />
                </div>

                <div class="form-group">
                  <label>Date sortie</label
                  ><input
                    v-model="object.checkout_date"
                    class="form-control"
                    type="date"
                    required
                  />
                </div>
                <div class="form-group">
                  <label>Date retour prévue</label
                  ><input
                    v-model="object.due_date"
                    class="form-control"
                    type="date"
                  />
                </div>
                <div class="form-group">
                  <label>Date retour</label
                  ><input
                    v-model="object.return_date"
                    class="form-control"
                    type="date"
                  />
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
import { mapGetters } from "vuex";
import InputDatalist from "@/components/InputDatalist";
import { EditMixin } from "@/common/mixins";
export default {
  name: "BookEdit",
  mixins: [EditMixin],
  components: {
    InputDatalist
  },
  data() {
    return {
      ressource: "loans",
      new_label: "Nouveau prêt",
      object_name: "Prêt"
    };
  },
  computed: {
    ...mapGetters({
      bookById: "books/byId",
      userById: "users/byId"
    })
  },
  methods: {
    get_empty() {
      var book = this.$route.query.bookid;
      if (!book) book = null;
      return {
        book: book,
        owner: null,
        checkout_date: null,
        due_date: null,
        return_date: null
      };
    },
    make_label() {
      var book = this.bookById(this.object.book);
      return (book ? book.prettytitle : "") + " " + this.object.borrowername;
    },
    makeUserLabel(item) {
      return item.username;
    },
    makeBookLabel(item) {
      return item ? item.prettytitle : "";
    }
  }
};
</script>
