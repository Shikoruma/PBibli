<template>
  <b-card v-bind:header="title">
    <b-card-body>
      <b-form-group >
        <b-form-checkbox-group class="checklist" v-bind:checked="checked" v-on:change="$emit('change',$event)" stacked switches>
          <slot v-for="item in items" name="checkitems" v-bind:item="item">
            <b-form-checkbox v-bind:value="item.id">
              {{ item.name }}
            </b-form-checkbox>
          </slot>
        </b-form-checkbox-group>
      </b-form-group>
    </b-card-body>
  </b-card>
</template>

<script>
  import { mapGetters } from "vuex";
  import { LOGOUT } from "@/store/actions.type";
  export default {
    name: "CheckList",
    props: ['title', 'items', 'checked'],
    data: function () {
      return {
        id: null,
      }
    },
    methods: {
    },
    mounted() {
      this.id = this._uid;
    },
  };
</script>
<style>
.checklist{
    text-align:left;
}
</style>
