<template>
  <div>
    <b-card-group deck>
      <SearchList title="Books" v-bind:items="books" v-slot="slotProps" v-if="!update && !add" v-on:select="selectObject" v-bind:searchFields="['title']" addbutton="true" v-on:add="addObject">
        {{ slotProps.item.title }}
      </SearchList>
    </b-card-group>

    <b-card-group deck v-if="update || add">
      <div class="card">
        <b-form @submit="saveObject">
          <div class="card-header">
            <b-row>
              <b-col>
                <b-button class="float-left" v-on:click="backtolist">Back</b-button>
              </b-col>
              <b-col>
                Book
              </b-col>
              <b-col>
                <template v-if="isAuthenticated">
                  <b-button class="float-right" type="submit" v-if="update" variant="primary">Update</b-button>
                  <b-button class="float-right" type="submit" v-if="add" variant="primary">Add</b-button>
                </template>
              </b-col>
            </b-row>
          </div>
          <b-card-body>
            <b-form-group id="isbn-group" label="ISBN:" label-for="isbn">
              <b-form-input id="ibns" v-model="book.isbn" required></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Titre:" label-for="input-1">
              <b-form-input id="input-1" v-model="book.title" required></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Autheur:" label-for="input-1">
              <b-form-input id="input-1" v-model="book.author" ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Titre Serie:" label-for="input-1">
              <b-form-input id="input-1" v-model="book.serie_title" ></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Numero tome:" label-for="input-1">
              <b-form-input id="input-1" v-model="book.num_volume" type="number" required></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Localisation:" label-for="input-1">
              <b-form-input id="input-1" v-model="book.localisation" ></b-form-input>
            </b-form-group>

            <b-form-group id="input-group-6" label="Demat" label-for="input-6">
              <b-form-checkbox id="input-6" v-model="book.demat" name="check-button" switch>
              </b-form-checkbox>
            </b-form-group>
            <b-form-group id="input-group-abs" label="Resumé:" label-for="input-abs">
              <b-form-textarea id="input-abs" v-model="book.abstract"></b-form-textarea>
            </b-form-group>

          </b-card-body>
        </b-form>
      </div>
    </b-card-group>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import { GET_BOOK, UPDATE_BOOK, CREATE_BOOK, FETCH_BOOKS, } from "@/store/actions.type";
  import { EditorMixin } from "@/common/mixins";
  import SearchList from "@/components/SearchList";
  import DynList from "@/components/DynList";

  export default {
    mixins: [EditorMixin],
    name: "Book",
    components: { SearchList, DynList },
    data() {
      return {
        emptyObject:{ num_volume: 1, demat:false },
        actions:{
          GET:GET_BOOK,
          UPDATE:UPDATE_BOOK,
          CREATE:CREATE_BOOK,
          FETCH:FETCH_BOOKS,
        },
        objectName:'Book',
      }
    },
    computed: {
      ...mapGetters(["books", "isAuthenticated"]),
      book(){
        return this.object
      },
    },
  };
</script>
