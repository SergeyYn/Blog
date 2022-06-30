<template>
    <ul v-if="posts">
        <li v-for="post in posts" :key="post.id" >
            <h3><router-link :to="{ name: 'post', params: { id: post.id }}">{{ post.title }}</router-link></h3>
            <strong>Category: </strong> <router-link :to="{ name: 'category', params: { id: post.category.id }}">{{ post.category.name }}</router-link>
            <br/>
            <strong>Posted by: </strong> {{ post.author.first_name }} {{ post.author.last_name }}
            <strong>At: </strong> {{ new Date(post.post_date).toLocaleString() }}
            <hr>
            <p class="post-list-fade">
            {{post.body}}</p>
            <br/>
        </li>
    </ul>
</template>

<script>


export default {
    props:{
        posts:{
            type: Array
        }
    }
}
</script>

<style>
</style>