<template>
  <h1>{{category}}</h1>
  <PostList :posts="posts"></PostList>
</template>

<script>
import PostList from '@/components/PostList.vue'
import axios from 'axios';

export default {
  name: 'CategoryView',
  components:{
    PostList,
  },
  data(){
    return{
        posts: [],
        category: ''
    }
  },
  created(){
    this.getCategoryPostList();
    this.getCategory();
  },
  methods:{
    getCategoryPostList(){
      axios
        .get('api/blog/posts/?cat=' + this.$route.params.id)
        .then(response => {
          this.posts = response.data;
          console.log(this.posts)
        })
        .catch(err=> {
            alert(err)
            console.log(err)
        })
    },
    getCategory(){
      axios
        .get('/api/blog/categories/' + this.$route.params.id)
        .then(response => {
          this.category = response.data.name;
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