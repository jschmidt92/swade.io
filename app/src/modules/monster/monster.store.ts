import { defineStore } from 'pinia'

export interface MonsterCreate {
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

export interface MonstersList {
  id: number
  name: string
  race: string
  gender: string
  damage: string | Record<string, any>
}

export interface MonsterUpdate {
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

export interface MonsterView {
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
  };
  quantity: number;
}

export interface NestedWeapon {
  weapon: {
    id: number;
    name: string;
    range: string;
    damage: string;
    rof: number;
    shots: number;
    min_str: string;
    wt: number;
    cost: number;
    notes: string;
  };
  quantity: number;
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

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'
// const BASE_URL = 'http://swadebot.api:8000/api'

export const useMonsterStore = defineStore('monster', {
  state: () => ({
    monster: null as MonsterView | null,
    monsters: [] as MonstersList[],
    error: null as string | null
  }),
  actions: {
    async createMonster(monster: MonsterCreate) {
      try {
        const response = await fetch(`${BASE_URL}/monsters`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(monster)
        })
        if (!response.ok) {
          throw Error('Could not create monster')
        }
        const newMonster = await response.json()
        this.monsters.push(newMonster)
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getMonsters() {
      try {
        let data = await fetch(`${BASE_URL}/monsters`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.monsters = await data.json()
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getMonster(id: any) {
      try {
        let data = await fetch(`${BASE_URL}/monsters/` + id)
        if (!data.ok) {
          throw Error('Monster does not exist')
        }
        this.monster = await data.json()
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async updateMonster(monster: MonsterUpdate) {
      try {
        const response = await fetch(`${BASE_URL}/monsters/${monster.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(monster)
        })
        if (!response.ok) {
          throw Error('Could not update monster')
        }
        const updatedMonster = await response.json()
        const index = this.monsters.findIndex(c => c.id === updatedMonster.id)
        if (index !== -1) {
          this.monsters.splice(index, 1, updatedMonster)
        }
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    }
  }
})
