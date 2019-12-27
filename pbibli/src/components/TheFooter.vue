<template>
  <footer>
    <div class="container">
      <router-link class="logo-font" :to="{ name: 'books', params: {} }">
        Bibli
      </router-link>
    </div>
  </footer>
</template>

<script>
export default {
  name: "RwvFooter"
};
</script>
