<template>
  <div v-if="post">
        <h1>{{post.title}}</h1>
        <strong>Posted by:</strong> {{ post.author.first_name }} {{ post.author.last_name }}
        <strong>At:</strong> {{ new Date(post.post_date).toLocaleString() }}
        <strong>Category:</strong> <router-link :to="{ name: 'category', params: { id: post.category.id }}">{{ post.category.name }}</router-link>
        <hr>
        {{post.body}}
        <br/><br/>
        <div v-if="checkAuthor">
            <button @click="this.$router.push('/post/' + post.id + '/edit/')" class="btn btn-primary">Update</button>
            <button @click="this.$router.push('/post/' + post.id + '/delete/')" class="btn btn-danger">Delete</button>
            <button @click="this.$router.push('/')" class="btn btn-secondary">Back</button>
        </div>
        <div v-else>
            <button @click="this.$router.push('/')" class="btn btn-secondary">Back</button>
        </div>
    </div>
</template>

<script>
export default {
    props:{
        post:{
            type: Object
        }
    },
    computed:{
        checkAuthor(){
            return this.post.author.id == this.$store.state.user_id
        }
    }
}
</script>

<style>

</style>