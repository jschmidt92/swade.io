import { createApp } from 'vue'
import { createPinia } from 'pinia'
import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import App from './App.vue'
import router from './router'

import './scss/style.scss'
import '../node_modules/bootstrap'

const app = createApp(App)
const pinia = createPinia()

import { faDiscord } from '@fortawesome/free-brands-svg-icons'
import { faEye, faPenToSquare, faPlus, faTrash, faThumbsUp, faThumbsDown, faXmark } from '@fortawesome/free-solid-svg-icons'

library.add(faDiscord, faEye, faPenToSquare, faPlus, faTrash, faThumbsUp, faThumbsDown, faXmark)

app.use(pinia)
app.use(router)
app.component('font-awesome-icon', FontAwesomeIcon)
app.mount('#app')
