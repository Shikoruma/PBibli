<template>
  <div class="card">
    <div class="card-header">
      <b-row>
        <b-col>
        </b-col>
        <b-col>
          {{ title }}
        </b-col>
        <b-col>
          <template v-if="isAuthenticated">
            <b-button v-if="addbutton" class="float-right" variant="primary" v-on:click="$emit('add')">Add</b-button>
          </template>
        </b-col>
      </b-row>
    </div>


    <b-card-body>
      <b-input-group>
        <b-form-input placeholder="Search" type="text" v-model="search"></b-form-input>
        <!--<b-input-group-append>
          <b-button variant="info">Search</b-button>
        </b-input-group-append>-->
      </b-input-group>
    </b-card-body>
    <b-list-group flush>
      <b-list-group-item v-on:click="$emit('select',item)" v-for="item in filteredItems" :key="item.id">
        <slot v-bind:item="item">
          {{ item.name }}
        </slot>
      </b-list-group-item>
    </b-list-group>
  </div>
</template>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  export default {
    name: "SearchList",
    props: ['title', 'items', 'searchFields', 'addbutton'],
    data: function () {
      return {
        search: '',
      }
    },
    computed: {
      ...mapGetters(["isAuthenticated"]),
      filteredItems() {
        if (typeof this.searchFields === 'function') {
          return this.searchFields(this.items,this.search);
        } else {
          return this.items.filter(item => {
            return this.searchFields.some((field) => {
              return item[field].toLowerCase().indexOf(this.search.toLowerCase()) > -1
            });
          })
        }
      },
    },
    methods: {}
  };
</script>
