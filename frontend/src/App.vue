<template>
  <NavBar/>
  <div class="container-md">
    <router-view/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
import axios from 'axios'
export default {
  name: 'App',
  components: {
    NavBar
  },
  created(){
    this.$store.commit('initializeStore');

    const token = this.$store.state.token;

    if(token){
      axios.defaults.headers.common['Authorization'] = "Token " + token;
    }
    else{
      axios.defaults.headers.common['Authorization'] = "";
    }
  }
}
</script>

<style>
.btn{
  margin: 0.2em;
}

.post-list-fade{
  display: -webkit-box;
  -webkit-mask-image: -webkit-gradient(linear, left 50%,
  left bottom, from(rgba(0,0,0,1)), to(rgba(0,0,0,0)));
  -webkit-line-clamp: 4;
  line-clamp: 4;
  -webkit-box-orient: vertical;
}

.error{
    margin-top: -.5em;
    margin-bottom: 1em;
    background: rgba(255,0,0,0.3);
    border: 2px solid rgba(255,0,0,0.2);
    color:rgba(50,0,0,1);
    border-radius: 0.2em;
    padding:0.2em;
}

.error:empty{
    display:none;
}

</style>
