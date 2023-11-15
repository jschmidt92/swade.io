import { defineStore } from 'pinia'

export interface NpcCreate {
  [key: string]: any
  name: string
  race: string
  gender: string
  charisma: number
  pace: number
  parry: number
  toughness: number
  attributes: string | Record<string, any>
  skills: string | Record<string, any>
  gear?: string | any[]
  hindrances: string
  edges: string
  cyberware?: string | Cyberware[]
  powers?: string | Power[]
  weapons?: string | NestedWeapon[]
  damage: string | Record<string, any>
  ammo: number
  money: number
}

export interface NpcsList {
  id: number
  name: string
  race: string
  gender: string
  damage: string | Record<string, any>
}

export interface NpcUpdate {
  id?: number
  name?: string
  race?: string
  gender?: string
  charisma?: number
  pace?: number
  parry?: number
  toughness?: number
  attributes?: string | Record<string, any>
  skills?: string | Record<string, any>
  gear?: string | NestedGear[]
  hindrances?: string
  edges?: string
  cyberware?: string | Cyberware[]
  powers?: string | Power[]
  weapons?: string | NestedWeapon[]
  damage?: string | Record<string, any>
  ammo?: number
  money?: number
}

export interface NpcView {
  name: string
  race: string
  gender: string
  charisma: number
  pace: number
  parry: number
  toughness: number
  attributes: string | Record<string, any>
  skills: string | Record<string, any>
  gear: NestedGear[]
  hindrances: string
  edges: string
  cyberware: Cyberware[]
  powers: Power[]
  weapons: NestedWeapon[]
  damage: Record<string, any>
  ammo: number
  money: number
}

export interface Cyberware {
  id: number
  name: string
  strain: number
  effect: string
  price: number
  notes: string
}

export interface Gear {
  id: number
  name: string
  min_str: string
  wt: number
  cost: number
  notes: string
}

export interface Power {
  id: number
  name: string
  pp: string
  range: string
  duration: string
  effect: string
  notes: string
}

export interface NestedGear {
  gear: {
    id: number
    name: string
    min_str: string
    wt: number
    cost: number
    notes: string
  }
  quantity: number
}

export interface NestedWeapon {
  weapon: {
    id: number
    name: string
    range: string
    damage: string
    rof: number
    shots: number
    min_str: string
    wt: number
    cost: number
    notes: string
  }
  quantity: number
}

export interface Weapon {
  id: number
  name: string
  range: string
  damage: string
  rof: number
  shots: number
  min_str: string
  wt: number
  cost: number
  notes: string
}

// const BASE_URL = 'https://apiv1.innovativedevsolutions.org'
const BASE_URL = 'http://135.135.196.140:8000'

export const useNpcStore = defineStore('npc', {
  state: () => ({
    npc: null as NpcView | null,
    npcs: [] as NpcsList[],
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
