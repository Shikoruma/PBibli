<template>
  <div id="app">
    <RwvHeader />
    <router-view></router-view>
    <RwvFooter />  
  </div>
</template>
<script>
import RwvHeader from "@/components/TheHeader";
import RwvFooter from "@/components/TheFooter";
import {TITLE} from "@/common/config";

export default {
  name: "App",
  components: {
    RwvHeader,
    RwvFooter
  },
  mounted() {
    document.title=TITLE;
  },


};
</script>
<style lang="less">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>


