<template>
  <div v-if="this.$store.state.isAuthenticated">
  </div>
</template>

<script>
  export default {
    name: 'LogoutView',
    created () {
      this.$store.commit('removeToken');
      this.$router.push({ name: 'home' });
    }
  }
</script>