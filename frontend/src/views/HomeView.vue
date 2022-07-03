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
        postsSocket: ''
    }
  },
  created(){
    this.connect();
  },
  methods:{
    connect(){
      let url = `ws://localhost:8000/ws/socket-server/posts/0`;
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
    }
  },
  beforeUnmount() {
    this.disconnect()
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
