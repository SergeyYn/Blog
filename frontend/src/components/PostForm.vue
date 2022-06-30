<template>
  <div v-if="this.$store.state.isAuthenticated">
    <form @submit.prevent="submitPostForm" class="register-form">
      <div class="form-group">
        <label for="Title">Title</label>
        <input type="text" name="Title" class="form-control" id="Title" v-model="formData.title">
      </div>
      <div class="form-group">
        <label for="Category">Category</label>
        <select class="form-control" id="Category" v-model="formData.category">
          <option disabled value="">Please select category</option>
          <option v-for="c in formData.categories" :text="c.name" :key="c.id" :value="c.id"></option>
        </select>
      </div>
      <div class="form-group">
        <label for="Body">Body</label>
        <textarea name="Body" class="form-control" id="Body" v-model="formData.body"></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
    props:{
        formData: {
            id: '',
            title: '',
            category: -1,
            body: '',
            categories:[]
        },
        requestType: ''
    },
    methods:{
        submitPostForm(){
            const requestData =  {
                title: this.formData.title,
                category_id: parseInt(this.formData.category, 10),
                body: this.formData.body,
                author_id: parseInt(this.$store.state.user_id, 10),
            }
            let axios_url = '/api/blog/posts' + (this.formData.id?'/' + this.formData.id + '/':'/');
            axios({
                method: this.requestType,
                url: axios_url,
                headers: {"Content-Type": "application/json"},
                data: requestData
            })
            .then(response => {
                this.$router.push({ name: 'home' });
            })
            .catch(err=> {
                console.log(err.response.data)
            })
        },
    }
}
</script>

<style>

</style>