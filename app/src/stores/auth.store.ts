import { defineStore } from 'pinia'

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'
// const BASE_URL = 'http://swade.api:4000'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isAuthenticated: false,
    token: '',
    discord_id: ''
  }),
  getters: {
    hasToken: (state) => {
      return !!state.token
    }
  },
  actions: {
    async loginWithDiscord() {
      try {
        window.location.href = `${BASE_URL}/discord/oauth2/login/`
      } catch (error) {
        console.error(error)
      }
    },
    logout() {
      this.setAuthenticated(false)
      localStorage.removeItem('token')
      localStorage.removeItem('discord_id')
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
    setDiscordId(discord_id: string) {
      this.discord_id = discord_id
      localStorage.setItem('discord_id', discord_id)
    },
    retrieveTokenAndDiscordId() {
      const url = new URL(window.location.href)
      const token = url.searchParams.get('token')
      const discord_id = url.searchParams.get('discord_id')
      if (token) {
        this.setToken(token)
      }
      if (discord_id) {
        this.setDiscordId(discord_id)
      }
    },
    getUser: async function (): Promise<any | null> {
      if (!this.discord_id) {
        return null
      }

      const response = await fetch(`${BASE_URL}/discord/${this.discord_id}/`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
          Authorization: `Bearer ${this.token}`
        }
      })

      if (!response.ok) {
        console.error('Failed to get user:', response)
        return null
      }

      const user = await response.json()
      return user
    }
  }
})
