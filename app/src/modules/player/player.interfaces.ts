import { NestedGear, NestedWeapon } from '@/modules/character/character.interfaces'

interface Character {
  id: number
  discordID: string
  name: string
  race: string
  gender: string
  money: number
  gear: NestedGear[]
  weapons: NestedWeapon[]
  damage: Record<string, any>
}

export type { Character }
