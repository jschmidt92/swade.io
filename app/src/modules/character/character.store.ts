import { defineStore } from 'pinia'

export interface CharacterCreate {
  [key: string]: any
  discordID: string | null
  name: string
  race: string
  gender: string
  charisma: number
  pace: number
  parry: number
  toughness: number
  attributes: Record<string, any>
  skills: Record<string, any>
  hindrances: string
  edges: string
  ammo: number
  money: number
}

export interface CharactersList {
  id: number
  discordID: number
  name: string
  race: string
  gender: string
  damage: Record<string, any>
}

export interface CharacterUpdate {
  id?: number
  discordID?: number
  name?: string
  race?: string
  gender?: string
  charisma?: number
  pace?: number
  parry?: number
  toughness?: number
  attributes?: Record<string, any>
  skills?: Record<string, any>
  gear?: NestedGear[]
  hindrances?: string
  edges?: string
  cyberware?: Cyberware[]
  powers?: Power[]
  weapons?: NestedWeapon[]
  damage?: Record<string, any>
  ammo?: number
  money?: number
}

export interface CharacterView {
  id: number
  discordID: number
  name: string
  race: string
  gender: string
  charisma: number
  pace: number
  parry: number
  toughness: number
  attributes: Record<string, any>
  skills: Record<string, any>
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

export const useCharacterStore = defineStore('character', {
  state: () => ({
    character: null as CharacterView | null,
    characters: [] as CharactersList[],
    error: null as string | null
  }),
  actions: {
    async createCharacter(character: CharacterCreate) {
      try {
        const response = await fetch(`${BASE_URL}/characters/new/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(character)
        })
        if (!response.ok) {
          throw Error('Could not create character')
        }
        const newCharacter = await response.json()
        this.characters.push(newCharacter)
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getCharacters() {
      try {
        let data = await fetch(`${BASE_URL}/characters/`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.characters = await data.json()
        return this.characters
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getCharacter(id: any) {
      try {
        let data = await fetch(`${BASE_URL}/characters/${id}/`)
        if (!data.ok) {
          throw Error('Character does not exist')
        }
        this.character = await data.json()
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async updateCharacter(character: CharacterUpdate) {
      try {
        const response = await fetch(
          `${BASE_URL}/characters/${character.id}/`,
          {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(character)
          }
        )
        if (!response.ok) {
          throw Error('Could not update character')
        }
        const updatedCharacter = await response.json()
        const index = this.characters.findIndex(
          (c) => c.id === updatedCharacter.id
        )
        if (index !== -1) {
          this.characters.splice(index, 1, updatedCharacter)
        }
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    }
  }
})
