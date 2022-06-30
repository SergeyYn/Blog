<template>
  <div v-if="this.$store.state.isAuthenticated">
    <h1>Are you sure you want to delete this post?</h1>
    <button class="btn btn-primary">Back</button>
    <button @click="deletePost" class="btn btn-danger">Delete</button>
    <hr/>
    <div>
      <h3>{{ post.title }}</h3>
      <strong>Category: </strong>{{ post.category.name }}
      <br/>
      <strong>Posted by: </strong> {{ post.author.first_name }} {{ post.author.last_name }}
      <strong>At: </strong> {{ new Date(post.post_date).toLocaleString() }}
      <hr>
      <p class="post-list-fade">
      {{post.body}}</p>
      <br/>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import PostDetails from '@/components/PostDetails.vue';
export default{
  name: 'PostDetails',
  components:{
    PostDetails
  },
  data(){
    return {
      post: {}
    }
  },
  created(){
    this.get_post_details();
  },
  methods:{
    get_post_details(){
      axios
          .get('/api/blog/posts/'+ this.$route.params.id)
          .then(response => {
              this.post = response.data;
          })
          .catch(err=> {
              alert(err)
              console.log(err)
          })
    },
    deletePost(){
      axios({
        method: "DELETE",
        url: '/api/blog/posts/' + this.post.id,
        headers: {"Content-Type": "application/json"}
      })
      .then(response => {
        console.log(response)
        this.$router.push({ name: 'home' });
      })
      .catch(err=> {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
</style>