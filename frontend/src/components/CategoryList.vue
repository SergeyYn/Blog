<template>
  <ul v-if="categories">
        <li v-for="c in categories" :key="c.id" >
            <h3><router-link :to="{ name: 'category', params: { id: c.id }}">{{ c.name }}</router-link></h3>
        </li>
    </ul>
</template>

<script>
export default {
    name: 'CategoryList',
    props:{
        categories:{
            type: Object
        }
    }
}
</script>

<style>

</style>