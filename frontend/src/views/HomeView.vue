<template>
  <div>
    <h1>Posts</h1>
    <PostList :posts="posts"></PostList>
  </div>
</template>

<script>
import PostList from '@/components/PostList.vue'
import axios from 'axios';

export default {
  name: 'HomeView',
  components:{
    PostList,
  },
  data(){
    return{
        posts: [],
    }
  },
  created(){
    this.getPostList();
  },
  methods:{
    getPostList(){
      axios
        .get('/api/blog/posts/')
        .then(response => {
            this.posts = response.data;
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
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
