import { ComputedRef, computed, reactive, ref, Ref } from 'vue'
import { useCharacterStore, type CharacterCreate } from './character.store'

interface Dictionary {
  name: string
  value: string
}

interface FormCharacterCreate
  extends Omit<CharacterCreate, 'attributes' | 'skills' | 'damage'> {
  attributes: Record<string, string>
  skills: Record<string, string>
  damage: string
}

export function useCharacterData() {
  const form = reactive<FormCharacterCreate>({
    discordID: '',
    name: '',
    race: '',
    gender: '',
    charisma: 0,
    pace: 0,
    parry: 0,
    toughness: 0,
    attributes: {},
    skills: {},
    hindrances: '',
    edges: '',
    damage: '{"Wounds": 0, "Fatigue": 0, "Inc": "No"}',
    ammo: 0,
    money: 0
  })

  const characterStore = useCharacterStore()
  const error = ref<string | null>(null)
  const isLoading = ref(false)

  const attribute = reactive({
    name: '',
    value: '',
    items: [] as Dictionary[]
  })

  const skill = reactive({
    name: '',
    value: '',
    items: [] as Dictionary[]
  })

  const genders = [
    { label: 'Male', value: 'male' },
    { label: 'Female', value: 'female' }
  ]

  const races = [
    { label: 'Android', value: 'android' },
    { label: 'Aquarian', value: 'aquarian' },
    { label: 'Aurax', value: 'aurax' },
    { label: 'Avion', value: 'avion' },
    { label: 'Construct', value: 'construct' },
    { label: 'Deader', value: 'deader' },
    { label: 'Dwarf', value: 'dwarf' },
    { label: 'Elf', value: 'elf' },
    { label: 'Floran', value: 'floran' },
    { label: 'Half-Elve', value: 'halfelve' },
    { label: 'Half-Folk', value: 'halffolk' },
    { label: 'Human', value: 'human' },
    { label: 'Insectoid', value: 'insectoid' },
    { label: 'Kalian', value: 'kalian' },
    { label: 'Rakashan', value: 'rakashan' },
    { label: 'Robot', value: 'robot' },
    { label: 'Saurian', value: 'saurian' },
    { label: 'Serran', value: 'serran' },
    { label: 'Yeti', value: 'yeti' }
  ]

  function jsonFormat(
    data: Ref<Dictionary[]>
  ): ComputedRef<Record<string, string>> {
    return computed(() => {
      const json: Record<string, string> = {}

      for (const item of data.value) {
        json[item.name] = item.value
      }

      return json
    })
  }

  const jsonFormatAttributes = jsonFormat(ref(attribute.items))
  const jsonFormatSkills = jsonFormat(ref(skill.items))

  function addAttribute() {
    form.attributes[attribute.name] = attribute.value
    attribute.items.push({ name: attribute.name, value: attribute.value })
    attribute.name = ''
    attribute.value = ''
  }

  const updateAttribute = (index: number): void => {
    const updatedAttribute = attribute.items[index]

    if (updatedAttribute) {
      updatedAttribute.name = updatedAttribute.name.trim()
      updatedAttribute.value = updatedAttribute.value.trim()
    }
  }

  const deleteAttribute = (index: number): void => {
    attribute.items.splice(index, 1)
  }

  function addSkill() {
    form.skills[skill.name] = skill.value
    skill.items.push({ name: skill.name, value: skill.value })
    skill.name = ''
    skill.value = ''
  }

  const updateSkill = (index: number): void => {
    const updatedSkill = skill.items[index]

    if (updatedSkill) {
      updatedSkill.name = updatedSkill.name.trim()
      updatedSkill.value = updatedSkill.value.trim()
    }
  }

  const deleteSkill = (index: number): void => {
    skill.items.splice(index, 1)
  }

  const create = async () => {
    if (
      !form.name ||
      !form.race ||
      !form.gender ||
      !form.charisma ||
      !form.pace ||
      !form.parry ||
      !form.toughness ||
      !form.hindrances ||
      !form.edges
    ) {
      error.value = 'Please fill in all required fields.'
      return
    }

    const userId = localStorage.getItem('discord_id')
    if (!userId) {
      error.value = 'Invalid Discord User ID.'
    }

    form.discordID = userId

    const jsonFields = ['damage']
    const parsedFields: Partial<CharacterCreate> = {}
    for (const field of jsonFields) {
      try {
        parsedFields[field] = JSON.parse(form[field])
      } catch (e) {
        error.value = `Invalid JSON in ${field} field`
        return
      }
    }

    const { attributes, skills, damage, ...otherFields } = form
    console.log(form)

    const characterData: CharacterCreate = {
      ...otherFields,
      ...parsedFields,
      attributes: jsonFormatAttributes.value,
      skills: jsonFormatSkills.value
    } as CharacterCreate

    isLoading.value = true
    try {
      await characterStore.createCharacter(characterData)
    } catch (e) {
      error.value = 'An error occurred while creating the character.'
    } finally {
      isLoading.value = false
    }
  }

  return {
    addAttribute,
    addSkill,
    attribute,
    create,
    deleteAttribute,
    deleteSkill,
    error,
    form,
    genders,
    isLoading,
    races,
    skill,
    updateAttribute,
    updateSkill
  }
}
