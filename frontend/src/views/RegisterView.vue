<template>
  <div v-if="!this.$store.state.isAuthenticated">
    <form @submit.prevent="registerUser" class="register-form">
      <div class="form-group">
        <label for="firstname">First name</label>
        <input type="text" name="firstname" class="form-control" id="firstname" v-model="first_name">
      </div>
      <p class="error">{{errors.first_name_error}}</p>
      <div class="form-group">
        <label for="lastname">Last name</label>
        <input type="text" name="lastname" class="form-control" id="lastname" v-model="last_name">
      </div>
      <p class="error">{{errors.last_name_error}}</p>
      <div class="form-group">
        <label for="el">Email</label>
        <input type="email" name="el" id="el" class="form-control" v-model="email">
      </div>
      <p class="error">{{errors.email_error}}</p>
      <div class="form-group">
        <label for="ur">Username</label>
        <input type="text" name="ur" id="ur" class="form-control" v-model="username">
      </div>
      <p class="error">{{errors.username_error}}</p>
      <div class="form-group">
        <label for="pwr">Password</label>
        <input type="password" name="pwr" class="form-control" id="pwr" v-model="password">
      </div>
      <p class="error">{{errors.password_error}}</p>
      <div class="form-group">
        <label for="pass">Password Confirmation</label>
        <input type="password" name="pass" class="form-control" id="pass" v-model="confirm">
      </div>
      <p class="error">{{errors.conf_password_error}}</p>
      <p class="error">{{errors.match_password_error}}</p>
      <button type="submit" class="btn btn-primary">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'RegisterView',
  data () {
    return {
      first_name: '',
      last_name: '',
      email: '',
      username: '',
      password: '',
      confirm: '',
      errors:{
        first_name_error: '',
        last_name_error: '',
        email_error: '',
        username_error: '',
        password_error: '',
        conf_password_error: '',
        match_password_error: '',
      }
    }
  },
  methods: {
    validateEmail(email) 
    {
        var re = /\S+@\S+\.\S+/;
        return re.test(email);
    },
    registerUser(){
      var correct = true;
      if(this.first_name == ''){
          this.errors.first_name_error = "First name can't be empty!";
          correct = false;
      }
      else{
          this.errors.first_name_error = '';
      }

      if(this.last_name == ''){
          this.errors.last_name_error = "Last name can't be empty!";
          correct = false;
      }
      else{
          this.errors.last_name_error = '';
      }

      if(this.username == ''){
          this.errors.username_error = "Username can't be empty!";
          correct = false;
      }
      else{
          this.errors.username_error = '';
      }

      if(!this.validateEmail(this.email)){
          this.errors.email_error  = "Invalid email!";
          correct = false;
      }
      else{
          this.errors.email_error = '';
      }

      if(this.password == ''){
          this.errors.password_error  = "Password can't be empty!!";
          correct = false;
      }
      else{
          this.errors.password_error = '';
      }

      if(this.confirm == ''){
          this.errors.conf_password_error  = "Password confirmation can't be empty!";
          correct = false;
      }
      else{
          this.errors.conf_password_error = '';
      }

      if(this.confirm != '' && this.password != '' && this.password != this.confirm){
          this.errors.match_password_error  = "Passwords don't match!";
          correct = false;
      }
      else{
          this.errors.match_password_error = '';
      }

      if(correct){
        const formData =  {
          first_name: this.first_name,
          last_name: this.last_name,
          username: this.username,
          email: this.email,
          username: this.username,
          password: this.password
        }
        axios({
          method: "POST",
          url: '/api/auth/users/',
          headers: {"Content-Type": "application/json"},
          data: formData
        })
        .then(response => {
          console.log(response)
          this.$router.push({ name: 'login' });
        })
        .catch(err=> {
          console.log(err)
        })
      }
    }
  }
}
</script>

<style scoped>
.register-form{
  margin-top:2em;
}
</style>