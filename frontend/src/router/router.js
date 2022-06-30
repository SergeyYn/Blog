
import HomeView from '@/views/HomeView.vue';
import CategoryListView from '@/views/CategoryListView.vue';
import CategoryView from '@/views/CategoryView.vue';
import PostDetailsView from '@/views/PostDetailsView.vue';
import CreatePostView from '@/views/CreatePostView.vue';
import EditPostView from '@/views/EditPostView.vue';
import DeletePostView from '@/views/DeletePostView.vue';
import LoginView from '@/views/LoginView.vue';
import LogoutView from '@/views/LogoutView.vue';
import AboutView from '@/views/AboutView.vue';
import RegisterView from '@/views/RegisterView.vue';

import { createRouter, createWebHistory } from 'vue-router';

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/category-list',
        name: 'category-list',
        component: CategoryListView
    },
    {
        path: '/category/:id',
        name: 'category',
        props: true,
        component: CategoryView
    },
    {
        path: '/post/:id',
        name: 'post',
        props: true,
        component: PostDetailsView
    },
    {
        path: '/post/create',
        name: 'create-post',
        component: CreatePostView
    },
    {
        path: '/post/:id/edit',
        name: 'edit-post',
        component: EditPostView
    },
    {
        path: '/post/:id/delete',
        name: 'delete-post',
        component: DeletePostView
    },
    
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },

    {
        path: '/logout',
        name: 'logout',
        component: LogoutView
    },
    
    {
        path: '/register',
        name: 'register',
        component: RegisterView
    },
    {
        path: '/about',
        name: 'about',
        component: AboutView
    },
]

const router = createRouter({
    routes,
    history: createWebHistory()
})

export default router;
