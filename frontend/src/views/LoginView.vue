<template>
  <div v-if="!this.$store.state.isAuthenticated">
    <div class="login-form">
      <div>
        <form v-on:submit.prevent="loginUser">
        <div class="form-group">
          <label for="user">Username</label>
          <input type="text" class="form-control" name="username" id="user" v-model="username">
        </div>
        <p class="error">{{login_error}}</p>
        <div class="form-group">
          <label for="pass">Password</label>
          <input type="password" class="form-control" name="password" id="pass" v-model="password">
        </div>
        <p class="error">{{pass_error}}</p>
        <p class="error">{{cred_error}}</p>
        <button type="submit" class="btn btn-primary">Login</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
  export default {
    name: 'login',
    data () {
      return {
        username: '',
        password: '',
        login_error:'',
        pass_error:'',
        cred_error:''
      }
    },
    methods: {
      loginUser () { // call loginUSer action
        const formData =  {
          username: this.username,
          password: this.password
        }  
        axios
            .post('/api/auth/token/login', formData)
            .then(response => {
              const token = response.data.auth_token;
              this.$store.commit('setToken', token);
              axios.defaults.headers.common['Authorization'] = "Token " + token;
              localStorage.setItem('token', token)
              axios
                  .get('/api/auth/users/me')
                  .then(response => {
                    localStorage.setItem('user_id', response.data.id);
                    this.$store.state.user_id = response.data.id;
                    this.notifyAdmin();
                    this.$router.push({ name: 'home' });
                  })
                  .catch(err=> {
                    console.log(err)
                  })
            })
            .catch(err=> {
              if(err.response.data['username'])
                this.login_error = err.response.data['username'][0];
              else
                this.login_error = '';
              if(err.response.data['password'])
                this.pass_error = err.response.data['password'][0];
              else
                this.pass_error = '';
              if(err.response.data['non_field_errors'])
                this.cred_error = err.response.data['non_field_errors'][0];
              else
                this.cred_error = '';
              console.log(err)
            })
      },
      notifyAdmin(){
        let url = `ws://localhost:8000/ws/socket-server/admin/users`;
        let userSocket = new WebSocket(url);
        userSocket.onopen = () => {
          userSocket.send(JSON.stringify({
            'action' : 'login',
            'id': this.$store.state.user_id}))
          userSocket.close()
        }
      }
    }
  }
</script>

<style scoped>
.login-form{
  margin-top:2em;
}
</style>