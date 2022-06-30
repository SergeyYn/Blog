<template>
  <div v-if="this.$store.state.isAuthenticated">
    <h1>Create post</h1>
    <PostForm :formData="formData" :requestType="'POST'"></PostForm>
    </div>
</template>

<script>
import axios from 'axios';
import PostForm from '@/components/PostForm.vue';
export default{
  name: 'CreatePostView',
  components:{
    PostForm
  },
  data(){
    return {
      formData:{
        id: '',
        title: '',
        category: {},
        body: '',
        categories:[]
      }
    }
  },
  created(){
    this.getCategoryList();
  },
  methods:{
    getCategoryList(){
      axios
        .get('/api/blog/categories/')
        .then(response => {
          this.formData.categories = response.data;
        })
        .catch(err=> {
          alert(err)
          console.log(err)
        })
      }
  }
}
</script>

<style scoped>
</style>