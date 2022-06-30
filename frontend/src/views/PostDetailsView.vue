<template>
    <PostDetails :post="post" v-if="post"></PostDetails>
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
            post: {},
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
        }
    }
}
</script>

<style scoped>
</style>