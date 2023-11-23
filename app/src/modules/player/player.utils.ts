import { onMounted, ref, Ref } from 'vue'
import { useCharacterStore } from '@/modules/character/character.store'
import { useAuthStore } from '@/stores/auth.store'
import { Character } from './player.interfaces'

export const usePlayerData = (): {
  characterStore: ReturnType<typeof useCharacterStore>
  characters: Ref<Character[] | undefined>
  getCurrentDateTime: () => string
  getPlayerCharacters: () => Promise<void>
  getPlayerInventory: () => { name: string; quantity: number }[]
  getPlayerWealth: () => string
} => {
  const authStore = useAuthStore()
  const characterStore = useCharacterStore()
  const discord_id = authStore.discord_id

  const characters: Ref<Character[] | undefined> = ref([])

  const getCurrentDateTime = (): string => {
    const currentDate = new Date()
    const options: Intl.DateTimeFormatOptions = {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    }
    return currentDate.toLocaleString(undefined, options)
  }

  const getPlayerCharacters = async () => {
    characters.value = (await characterStore.getPlayerCharacters(
      discord_id
    )) as Character[]
  }

  const getPlayerInventory = (): { name: string; quantity: number }[] => {
    const inventory: { name: string; quantity: number }[] = []
    const itemMap: Map<string, number> = new Map()

    characters.value?.forEach((character) => {
      character.gear.forEach((item) => {
        const itemName = item.gear.name
        const itemQuantity = item.quantity
        if (itemMap.has(itemName)) {
          itemMap.set(itemName, itemMap.get(itemName)! + itemQuantity)
        } else {
          itemMap.set(itemName, itemQuantity)
        }
      })
      character.weapons.forEach((weapon) => {
        const weaponName = weapon.weapon.name
        const weaponQuantity = weapon.quantity
        if (itemMap.has(weaponName)) {
          itemMap.set(weaponName, itemMap.get(weaponName)! + weaponQuantity)
        } else {
          itemMap.set(weaponName, weaponQuantity)
        }
      })
    })

    itemMap.forEach((quantity, name) => {
      inventory.push({ name, quantity })
    })

    return inventory
  }

  const getPlayerWealth = (): string => {
    let total = 0
    characters.value?.forEach((character) => {
      total += character.money
    })
    return total.toLocaleString(undefined, {
      minimumFractionDigits: 2,
      maximumFractionDigits: 2
    })
  }

  onMounted(async () => {
    await getPlayerCharacters()
  })

  return {
    characterStore,
    characters,
    getCurrentDateTime,
    getPlayerCharacters,
    getPlayerInventory,
    getPlayerWealth
  }
}
