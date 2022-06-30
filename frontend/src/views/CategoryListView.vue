<template>
  <h1>Blog categories</h1>
  <CategoryList :categories="categories"></CategoryList>
</template>

<script>
import axios from 'axios';
import CategoryList from '@/components/CategoryList'
export default{
  name: 'CategoryListView',
  components:{
    CategoryList
  },
  data(){
    return{
      categories: []
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
          this.categories = response.data;
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