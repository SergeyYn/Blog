<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
    <router-link class="navbar-brand" to='/'>Super blog</router-link>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul v-if="this.$store.state.isAuthenticated" class="navbar-nav mr-auto">
        <li class="nav-item">
            <router-link class="nav-link" to='/about' @click="closeMenu($event)">About</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/category-list' @click="closeMenu($event)">Categories</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/post/create' @click="closeMenu($event)">Create new post</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/category/create' @click="closeMenu($event)">Create new category</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/logout' @click="closeMenu($event)">Log out</router-link>
        </li>
      </ul>
      <ul v-else class="navbar-nav mr-auto">
        <li class="nav-item">
            <router-link class="nav-link" to='/category-list' @click="closeMenu($event)">Categories</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/login' @click="closeMenu($event)">Log in</router-link>
        </li>
        <li class="nav-item">
            <router-link class="nav-link" to='/register' @click="closeMenu($event)">Register</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {    
    name: 'NavBar',
    methods: {
      closeMenu($event) {
          $($event.currentTarget).closest('.navbar-collapse').collapse('hide');
      }    
   }
}
</script>

<style>

</style>