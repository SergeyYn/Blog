import { createApp } from 'vue'
import App from './App.vue'
import axios from 'axios'
import router from '@/router/router'
import store from '@/store/'

axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)

app 
    .use(store)
    .use(router, axios)
    .mount('#app')
