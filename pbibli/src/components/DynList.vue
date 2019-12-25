<template>
  <b-card v-bind:header="title">
    <b-card-body>
      <b-form @submit="$emit('add', search)">
        <b-input-group>
          <input class="form-control" :list="id" v-model="search"></input>
          <datalist :id="id">
            <slot v-for="sitem in searchitems" name="searchitem" v-bind:sitem="sitem">
              <option v-bind:value="sitem.id">
                {{ sitem.name }}
              </option>
            </slot>
          </datalist>
          <b-input-group-append>
            <b-button type="submit" variant="info">Add</b-button>
          </b-input-group-append>
        </b-input-group>
      </b-form>
    </b-card-body>
    <b-list-group flush>
      <b-list-group-item class="text-left" v-for="item in items">
        <slot v-bind:item="item">
          {{ item.name }}
        </slot>
        <b-button variant="info" class="float-right" v-on:click="$emit('delete',item)">Delete</b-button>
      </b-list-group-item>
    </b-list-group>
  </b-card>
</template>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  export default {
    name: "DynList",
    props: ['title', 'items', 'searchitems'],
    data: function () {
      return {
        search: '',
        id: null,
      }
    },
    mounted() {
      this.id = this._uid;

    },
    methods: {}
  };
</script>
