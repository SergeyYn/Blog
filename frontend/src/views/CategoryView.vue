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
  mounted(){
    this.connect();
    this.getCategory();
  },
  methods:{
    connect(){
      let url = `ws://localhost:8000/ws/socket-server/posts/` + this.$route.params.id;
      this.postsSocket = new WebSocket(url);
      this.postsSocket.onopen = () => {
      }
      this.postsSocket.onmessage = ({data}) => {
        console.log('SOCKET DATA: ', JSON.parse(data));
        this.posts = JSON.parse(data)
      }
    },
    disconnect(){
      this.postsSocket.close()
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
  },
  beforeUnmount() {
    this.disconnect()
  }
}

</script>

<style scoped>
</style>