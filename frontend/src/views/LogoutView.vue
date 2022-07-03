<template>
  <div v-if="this.$store.state.isAuthenticated">
  </div>
</template>

<script>
  export default {
    name: 'LogoutView',
    mounted () {
      let id = this.$store.state.user_id;
      this.notifyAdmin(id);
      this.$store.commit('removeToken');
      this.$router.push({ name: 'home' });
    },
    methods:{
      notifyAdmin(id){
        let url = `ws://localhost:8000/ws/socket-server/admin/users`;
        let userSocket = new WebSocket(url);
        userSocket.onopen = async () => {
          userSocket.send(JSON.stringify({
            'action' : 'logout',
            'id': id}))
          userSocket.close()
        }
      }
    }
  }
</script>