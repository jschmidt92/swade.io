import { defineStore } from 'pinia'
import {
  NpcCreate,
  NpcList,
  NpcUpdate,
  NpcView
} from './npc.interfaces'

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'

export const useNpcStore = defineStore('npc', {
  state: () => ({
    npc: null as NpcView | null,
    npcs: [] as NpcList[],
    error: null as string | null
  }),
  actions: {
    async createNpc(npc: NpcCreate) {
      try {
        const response = await fetch(`${BASE_URL}/npcs/new/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(npc)
        })
        if (!response.ok) {
          throw Error('Could not create npc')
        }
        const newNpc = await response.json()
        this.npcs.push(newNpc)
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getNpcs() {
      try {
        let data = await fetch(`${BASE_URL}/npcs/`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.npcs = await data.json()
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getNpc(id: any) {
      try {
        let data = await fetch(`${BASE_URL}/npcs/${id}/`)
        if (!data.ok) {
          throw Error('Npc does not exist')
        }
        this.npc = await data.json()
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async updateNpc(npc: NpcUpdate) {
      try {
        const response = await fetch(`${BASE_URL}/npcs/${npc.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(npc)
        })
        if (!response.ok) {
          throw Error('Could not update npc')
        }
        const updatedNpc = await response.json()
        const index = this.npcs.findIndex((c) => c.id === updatedNpc.id)
        if (index !== -1) {
          this.npcs.splice(index, 1, updatedNpc)
        }
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    }
  }
})
