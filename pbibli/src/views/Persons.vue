<template>
  <div>
    <b-card-group deck>
      <SearchList title="Person" v-bind:items="persons" v-slot="slotProps" v-if="!update && !add" v-on:select="selectObject" v-bind:searchFields="['name','nickname']" addbutton="true" v-on:add="addObject">
        {{ slotProps.item.nickname }}
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
                  <b-button class="float-right" type="submit" v-if="update" variant="primary">Update</b-button>
                  <b-button class="float-right" type="submit" v-if="add" variant="primary">Add</b-button>
              </b-col>
            </b-row>
          </div>
          <b-card-body>
            <b-form-group id="isbn-group" label="Pseudo:" label-for="isbn">
              <b-form-input id="ibns" v-model="person.nickname" required></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Nom:" label-for="input-1">
              <b-form-input id="input-1" v-model="person.name" required></b-form-input>
            </b-form-group>
            <b-form-group id="input-group-1" label="Contact:" label-for="input-1">
              <b-form-input id="input-1" v-model="person.contact" ></b-form-input>
            </b-form-group>
          </b-card-body>
        </b-form>
      </div>
    </b-card-group>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import { GET_PERSON, UPDATE_PERSON, CREATE_PERSON, FETCH_PERSONS, } from "@/store/actions.type";
  import { EditorMixin } from "@/common/mixins";
  import SearchList from "@/components/SearchList";
  import DynList from "@/components/DynList";

  export default {
    mixins: [EditorMixin],
    name: "Person",
    components: { SearchList, DynList },
    data() {
      return {
        emptyObject:{ },
        actions:{
          GET:GET_PERSON,
          UPDATE:UPDATE_PERSON,
          CREATE:CREATE_PERSON,
          FETCH:FETCH_PERSONS,
        },
        objectName:'Person',
      }
    },
    computed: {
      ...mapGetters(["persons", "isAuthenticated"]),
      person(){
        return this.object
      },
    },
  };
</script>
