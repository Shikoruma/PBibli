<template>
  <div>
    <b-card-group deck>
      <SearchList title="Loans" v-bind:items="loans" v-slot="slotProps" v-if="!update && !add" v-on:select="selectObject" v-bind:searchFields="searchLoans" addbutton="true" v-on:add="addObject">
        {{ person_dict[slotProps.item.person]? person_dict[slotProps.item.person].nickname:'' }}
        {{ book_dict[slotProps.item.book]? book_dict[slotProps.item.book].title:'' }}
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
                Loan
              </b-col>
              <b-col>
                <b-button class="float-right" type="submit" v-if="update" variant="primary">Update</b-button>
                <b-button class="float-right" type="submit" v-if="add" variant="primary">Add</b-button>
              </b-col>
            </b-row>
          </div>
          <b-card-body>
          <b-form-group label="Personne">
            <b-form-select v-model="loan.person" required>
              <option v-for="p in persons" v-bind:value="p.id" v-text="p.nickname" />
            </b-form-select>
          </b-form-group>
          <BookInput v-model="loan.book" />
          
          <b-form-group id="input-group-1" label="loan date:" label-for="input-1">
            <b-form-input id="input-1" v-model="loan.loan_date" type="date" required></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-1" label="due date:" label-for="input-1">
            <b-form-input id="input-1" v-model="loan.due_date" type="date"></b-form-input>
          </b-form-group>
          <b-form-group id="input-group-1" label="return date:" label-for="input-1">
            <b-form-input id="input-1" v-model="loan.return_date" type="date"></b-form-input>
          </b-form-group>
          </b-card-body>
        </b-form>
      </div>
    </b-card-group>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import { GET_LOAN, UPDATE_LOAN, CREATE_LOAN, FETCH_LOANS, FETCH_PERSONS, FETCH_BOOKS } from "@/store/actions.type";
  import { EditorMixin } from "@/common/mixins";
  import SearchList from "@/components/SearchList";
  import DynList from "@/components/DynList";
  import BookInput from "@/components/BookInput";

  export default {
    mixins: [EditorMixin],
    name: "Loan",
    components: { SearchList, DynList, BookInput },
    data() {
      return {
        emptyObject:{loan_date:(new Date()).toISOString().replace(/T.*/, "") },
        actions:{
          GET:GET_LOAN,
          UPDATE:UPDATE_LOAN,
          CREATE:CREATE_LOAN,
          FETCH:FETCH_LOANS,
        },
        objectName:'Loan',
      }
    },
    computed: {
      ...mapGetters(["loans", "books", "persons", "isAuthenticated"]),
      loan(){
        return this.object
      },
      person_dict: function () {
        var ret = {}
        this.persons.forEach(person => {
          ret[person.id] = person;
        });
        return ret
      },
      book_dict: function () {
        var ret = {}
        this.books.forEach(book => {
          ret[book.id] = book;
        });
        return ret
      },
    },
    methods: {
        searchLoans(items,search){
          return items.filter(item => {
            if (search.length == 0) return true;
            search = search.toLowerCase()
            var book=this.book_dict[item.book]
            if(book.serie_title && book.serie_title.toLowerCase().indexOf(search) > -1) return true 
            return this.person_dict[item.person].nickname.toLowerCase().indexOf(search) > -1 || book.title.toLowerCase().indexOf(search) > -1;
          })
        },
    },
    beforeMount() {
      this.$store.dispatch(FETCH_PERSONS);
      this.$store.dispatch(FETCH_BOOKS);
    },
  };
</script>
