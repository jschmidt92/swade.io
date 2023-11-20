interface CharacterCreate {
  [key: string]: any
  discordID: string
  name: string
  race: string
  gender: string
  charisma: number
  pace: number
  parry: number
  toughness: number
  attributes: Record<string, string>
  skills: Record<string, string>
  hindrances: string
  edges: string
  ammo: number
  money: number
}

interface CharacterList {
  id: number
  discordID: string
  name: string
  race: string
  gender: string
  damage: Record<string, number | string>
}

interface CharacterUpdate extends Partial<Omit<CharacterCreate, 'attributes' | 'skills' | 'damage'>> {
  id: number
  gear?: NestedGear[]
  cyberware?: Cyberware[]
  powers?: Power[]
  weapons?: NestedWeapon[]
}

interface CharacterView extends CharacterCreate {
  id: number
  gear: NestedGear[]
  cyberware: Cyberware[]
  powers: Power[]
  weapons: NestedWeapon[]
}

interface Cyberware {
  id: number
  name: string
  strain: number
  effect: string
  price: number
  notes: string
}

interface Gear {
  id: number
  name: string
  min_str: string
  wt: number
  cost: number
  notes: string
}

interface Power {
  id: number
  name: string
  pp: string
  range: string
  duration: string
  effect: string
  notes: string
}

interface NestedGear {
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

interface NestedWeapon {
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

interface Weapon {
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

interface Attribute {
  name: string
  value: string
  items?: Dictionary[]
}

interface Dictionary {
  name: string
  value: string
}

interface Skill {
  name: string
  value: string
  items?: Dictionary[]
}

interface FormCharacterCreate extends Omit<CharacterCreate, 'attributes' | 'skills' | 'damage'> {
  attributes: Record<string, string>
  skills: Record<string, string>
  damage: string
}

enum Gender {
  male = 'Male',
  female = 'Female'
}

enum Race {
  android = 'Android',
  aquarian = 'Aquarian',
  aurax = 'Aurax',
  avion = 'Avion',
  construct = 'Contruct',
  deader = 'Deader',
  dwarf = 'Dwarf',
  elf = 'Elf',
  floran = 'Floran',
  halfElve = 'Half-Elve',
  halfFolk = 'Half-Folk',
  human = 'Human',
  insectoid = 'Insectoid',
  kalian = 'Kalian',
  rakashan = 'Rakashan',
  robot = 'Robot',
  saurian = 'Saurian',
  serran = 'Serran',
  yeti = 'Yeti'
}

export type {
  Attribute,
  CharacterCreate,
  CharacterList,
  CharacterUpdate,
  CharacterView,
  Dictionary,
  FormCharacterCreate,
  Gear,
  NestedGear,
  NestedWeapon,
  Skill,
  Weapon
}
export { Gender, Race }
