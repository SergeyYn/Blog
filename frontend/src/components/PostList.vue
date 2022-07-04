<template>
    <div v-show="loaded">
        <ul>
            <li v-for="post in posts" :key="post.id" >
                <h3><router-link :to="{ name: 'post', params: { id: post.id }}">{{ post.title }}</router-link></h3>
                <strong>Category: </strong> <router-link :to="{ name: 'category', params: { id: post.category.id }}">{{ post.category.name }}</router-link>
                <br/>
                <strong>Posted by: </strong> <span>{{ post.author.first_name }} {{ post.author.last_name }}</span>
                <strong> At: </strong> {{ new Date(post.post_date).toLocaleString() }}
                <hr>
                <p class="post-list-fade">
                {{post.body}}</p>
                <br/>
            </li>
        </ul>
    </div>
</template>

<script>


export default {
    props:{
        posts:{
            type: Array
        },
        loaded: false
    }
}
</script>

<style>
</style>