<template>
  <div v-if="this.$store.state.isAuthenticated">
    <h1>Edit post</h1>
    <PostForm :formData="formData" :requestType="'PATCH'"></PostForm>
  </div>
</template>

<script>
import axios from 'axios';
import PostForm from '@/components/PostForm.vue';
export default{
  name: 'EditPostView',
  components:{
    PostForm
  },
  data(){
    return {
      formData:{
        id: this.$route.params.id,
        title: '',
        category: -1,
        body: '',
        categories:[]
      }
    }
  },
  created(){
    this.getCategoryList();
    this.get_post_details();
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
    },
    get_post_details(){
        axios
            .get('/api/blog/posts/'+ this.$route.params.id)
            .then(response => {
                let post = response.data;
                this.formData.title = post.title;
                this.formData.category = post.category.id;
                this.formData.body = post.body;
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