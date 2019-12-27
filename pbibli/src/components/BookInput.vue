<template>
  <b-form-group id="user-lab" label="Book: " label-for="book">
      <b-form-row class="align-items-center">
      <b-col>
        <label class="align-middle" for="book"> {{ title }}</label>
      </b-col>
      <b-col>
        <input class="form-control" id="user" list="books" v-bind:value="value" v-on:input="$emit('input', $event.target.value)" required></input>
        <datalist id="books">
          <option v-for="book in books" :value="book.id">
             {{ book.title }} {{ book.author }}
          </option>
        </datalist>
      </b-col>
    </b-form-row>
  </b-form-group>
</template>

<script>
  import { mapGetters } from "vuex";
  import { FETCH_BOOKS } from "@/store/actions.type";
  export default {
    name: "BookInput",
    props: ['value', ],
    data: function () {
      return {
        id: null,
      }
    },
    computed: {
      ...mapGetters(["books"]),
      title() {
        if (this.value in this.book_dict) {
          return this.book_dict[this.value].title
        } else {
          return ''
        }

      },
      book_dict: function () {
        var ret = {}
        this.books.forEach(book => {
          ret[book.id] = book;
        });
        return ret
      },

    },
    beforeMount() {
      this.$store.dispatch(FETCH_BOOKS);
    },
    mounted() {
      this.id = this._uid;

    },
  };
</script>
