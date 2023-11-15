<template>
  <div>
    <ul class="navbar-nav ms-auto" v-if="authStore.isAuthenticated">
      <li class="nav-item dropdown">
        <a
          class="nav-link dropdown-toggle"
          href="#"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          >{{ username }}</a
        >
        <ul class="dropdown-menu">
          <router-link
            class="dropdown-item"
            :to="`/player/dashboard`"
            >Dashboard</router-link
          >
          <router-link class="dropdown-item" to="/" @click="authStore.logout"
            >Logout</router-link
          >
          <template v-if="is_gm">
            <li><hr class="dropdown-divider border-light" /></li>
            <router-link class="dropdown-item" to="/Npcs"
              >View NPCs</router-link
            >
            <router-link class="dropdown-item" to="/Npcs/create"
              >Create NPC</router-link
            >
            <li><hr class="dropdown-divider border-light" /></li>
            <router-link class="dropdown-item" to="/encounters"
              >View Encounters</router-link
            >
            <router-link class="dropdown-item" to="/encounters/create"
              >Create Encounter</router-link
            >
          </template>
        </ul>
      </li>
    </ul>
    <button
      class="btn btn-outline-light"
      v-else
      @click="authStore.loginWithDiscord"
    >
      Login with Discord
    </button>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref, watchEffect } from 'vue'
import { useAuthStore } from '@/stores/auth.store'

const authStore = useAuthStore()
const username = ref('')
const is_gm = ref(false)

interface User {
  global_name?: string
  is_gm?: boolean
}

const getUser = async () => {
  const user = (await authStore.getUser()) as User
  if (user) {
    username.value = user.global_name || 'Unknown'
    is_gm.value = user.is_gm || false
  }
}

watchEffect(() => {
  if (authStore.isAuthenticated && authStore.discord_id) {
    getUser()
  }
})

onMounted(async () => {
  authStore.retrieveTokenAndDiscordId()
})
</script>
