import { defineStore } from 'pinia'

const BASE_URL = 'http://localhost:8000'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    token: '',
    discordID: '',
  }),
  getters: {
    hasToken: (state) => {
      return !!state.token
    }
  },
  actions: {
    async loginWithDiscord() {
      try {
        window.location.href = "http://localhost:8000/discord/oauth2/login/"
      } catch (error) {
        console.error(error)
      }
    },
    logout() {
      this.setAuthenticated(false)
      localStorage.removeItem('token')
      localStorage.removeItem('discordID')
      window.location.href = '/'
    },
    setAuthenticated(authenticated: boolean) {
      this.isAuthenticated = authenticated
    },
    setToken(token: string) {
      this.token = token
      this.isAuthenticated = true
      localStorage.setItem('token', token)
    },
    setDiscordId(discordID: string) {
      this.discordID = discordID
      localStorage.setItem('discordID', discordID)
    },
    retrieveTokenAndDiscordId() {
      const url = new URL(window.location.href)
      const token = url.searchParams.get('token')
      const discordID = url.searchParams.get('discord_id')
      if (token) {
        this.setToken(token)
      }
      if (discordID) {
        this.setDiscordId(discordID)
      }
    },
    getUsername: async function (): Promise<string | null> {
      if (!this.discordID) {
        console.error('No Discord ID found in local storage.')
        return null
      }

      const response = await fetch(`${BASE_URL}/discord/${this.discordID}/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${this.token}`
        }
      })

      if (!response.ok) {
        console.error('Failed to get username:', response)
        return null
      }

      const user = await response.json()
      return user.global_name
    }
  }
})