import { defineStore } from 'pinia'
import {
  CharacterCreate,
  CharacterList,
  CharacterUpdate,
  CharacterView
} from './character.interfaces'

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'

export const useCharacterStore = defineStore('character', {
  state: () => ({
    character: null as CharacterView | null,
    characters: [] as CharacterList[],
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
        console.log(newCharacter)
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
    async getPlayerCharacters(id: string) {
      try {
        let data = await fetch(`${BASE_URL}/characters/list/${id}/`)
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
