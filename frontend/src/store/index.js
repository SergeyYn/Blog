import {createStore} from 'vuex';

export default createStore({
    state:{
        token: '',
        user_id: -1,
        isAuthenticated: false
    },
    mutations:{
        initializeStore(state){
            if(localStorage.getItem('token')){
                state.token = localStorage.getItem('token');
                state.isAuthenticated = true;
                state.user_id = localStorage.getItem('user_id');
            }
            else{
                state.token = '';
                state.isAuthenticated = false;
                state.user_id = -1;
            }
        },
        setToken(state, token){
            state.token = token;
            state.isAuthenticated = true;
        },
        removeToken(state){
            state.token = '';
            state.isAuthenticated = false;
            state.user_id = -1;
        }
    },
    actions:{

    },
    modules:{

    }

    /*state:{
        accessToken: localStorage.getItem('access_token') || null, // makes sure the user is logged in even after
        // refreshing the page
        refreshToken: localStorage.getItem('refresh_token') || null,
        APIData: '' // received data from the backend API is stored here.
    },
    getters:{
        loggedIn (state) {
            return state.accessToken != null
        }
    },
    mutations:{
        updateLocalStorage (state, { access, refresh }) {
            localStorage.setItem('access_token', access)
            localStorage.setItem('refresh_token', refresh)
            state.accessToken = access
            state.refreshToken = refresh
        },
        updateAccess (state, access) {
            state.accessToken = access
        },
        destroyToken (state) {
            state.accessToken = null
            state.refreshToken = null
        }
    },
    actions:{
        refreshToken (context) {
            return new Promise((resolve, reject) => {
                axiosBase.post('/api/token/refresh/', {
                refresh: context.state.refreshToken
                }) // send the stored refresh token to the backend API
                .then(response => { // if API sends back new access and refresh token update the store
                    console.log('New access successfully generated')
                    context.commit('updateAccess', response.data.access)
                    resolve(response.data.access)
                })
                .catch(err => {
                    console.log('error in refreshToken Task')
                    reject(err) // error generating new access and refresh token because refresh token has expired
                })
            })
        },
        registerUser (context, data) {
            return new Promise((resolve, reject) => {
                axiosBase.post('/api/users/register', {
                    first_name: data.first_name,
                    last_name: data.last_name,
                    email: data.email,
                    username: data.username,
                    password: data.password,
                    confirm: data.confirm
                })
                .then(response => {
                    resolve(response)
                })
                .catch(error => {
                    reject(error)
                })
            })
        },
        logoutUser (context) {
            if (context.getters.loggedIn) {
                return new Promise((resolve, reject) => {
                axiosBase.post('/api/token/logout/')
                    .then(response => {
                        localStorage.removeItem('access_token')
                        localStorage.removeItem('refresh_token')
                        context.commit('destroyToken')
                    })
                    .catch(err => {
                        localStorage.removeItem('access_token')
                        localStorage.removeItem('refresh_token')
                        context.commit('destroyToken')
                        resolve(err)
                    })
                })
            }
        },
        loginUser (context, credentials) {
            return new Promise((resolve, reject) => {
                // send the username and password to the backend API:
                axiosBase.post('/api/token/', {
                    username: credentials.username,
                    password: credentials.password
                })
                // if successful update local storage:
                .then(response => {
                    context.commit('updateLocalStorage', { access: response.data.access, refresh: response.data.refresh }) 
                    resolve(response)
                })
                .catch(err => {
                    reject(err)
                })
            })
        }
    }*/
})