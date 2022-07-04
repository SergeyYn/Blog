<template>
    <PostDetails v-if="loaded" :post="post" :loaded="loaded"></PostDetails>
</template>

<script>
import axios from 'axios';
import PostDetails from '@/components/PostDetails.vue'
export default {
    components:{
        PostDetails
    },
    data(){
        return{
            post:{},
            loaded: false
        }
    },
    async mounted(){
        await this.get_post_details()
    },
    methods:{
        async get_post_details(){
            try{
                let response = await axios.get('/api/blog/posts/'+ this.$route.params.id)
                this.post = response.data;
                this.loaded = true;
            }
            catch(error){
                alert(err)
                   console.log(err)
            }
             //await axios.get('/api/blog/posts/'+ this.$route.params.id)
             //  .then((response) => {
             //      console.log(response)
             //      if(response.data.id)
             //          this.post = response.data;
             //          this.loaded = true;
             //  })
             //  .catch((err)=> {
             //      alert(err)
             //      console.log(err)
             //  })
        }
    }
}
</script>

<style scoped>
</style>