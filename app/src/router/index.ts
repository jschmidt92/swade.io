import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import AboutView from '@/views/AboutView.vue'
import SwadeView from '@/views/SwadeView.vue'
import SwadeSFCView from '@/views/SwadeSFCView.vue'
import { characterRoutes } from '@/modules/character'
import { encounterRoutes } from '@/modules/encounter'
import { monsterRoutes } from '@/modules/monster'
import { useAuthStore } from '@/stores/auth.store'

const router =  createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        { path: '/', name: 'home', component: HomeView },
        { path: '/about', name: 'about', component: AboutView },
        { path: '/swade', name: 'swade', component: SwadeView },
        { path: '/swade-sfc', name: 'swade-sfc', component: SwadeSFCView },
        ...characterRoutes,
        ...encounterRoutes,
        ...monsterRoutes
    ]
})

router.beforeEach((to, from, next) => {
    const authStore = useAuthStore()
    const token = localStorage.getItem('token')
    const discord_id = localStorage.getItem('discordId')

    if (token) {
        authStore.setToken(token || '')
        authStore.setDiscordId(discord_id || '')
        authStore.setAuthenticated(true)
    } else {
        authStore.setToken('')
        authStore.setDiscordId('')
        authStore.setAuthenticated(false)
    }

    next()
})

export default router