import { ComputedRef, computed, reactive, ref, Ref } from 'vue'
import { useNpcStore } from './npc.store'
import {
  Attribute,
  Dictionary,
  Faction,
  FormNpcCreate,
  Gender,
  NpcCreate,
  Race,
  Skill
} from './npc.interfaces'
import { useAuthStore } from '@/stores/auth.store'

export function convertEnumToArray(
  enumObject: Record<string, string>
): { label: string; value: string }[] {
  return Object.keys(enumObject).map((key) => ({
    label: enumObject[key],
    value: key
  }))
}

export function useNpcData() {
  const form = reactive<FormNpcCreate>({
    name: '',
    race: '',
    gender: '',
    faction: '',
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

  const authStore = useAuthStore()
  const npcStore = useNpcStore()
  const error = ref<string | null>(null)
  const isLoading = ref(false)

  const attributes = reactive<Attribute>({
    name: '',
    value: '',
    items: []
  })

  const skills = reactive<Skill>({
    name: '',
    value: '',
    items: []
  })

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

  function addAttribute() {
    form.attributes[attributes.name] = attributes.value
    attributes.items?.push({ name: attributes.name, value: attributes.value })
    attributes.name = ''
    attributes.value = ''
  }

  function updateAttribute(index: number): void {
    const updatedAttribute = attributes.items && attributes.items[index]

    if (updatedAttribute) {
      updatedAttribute.name = updatedAttribute.name.trim()
      updatedAttribute.value = updatedAttribute.value.trim()
    }
  }

  function deleteAttribute(index: number): void {
    attributes.items?.splice(index, 1)
  }

  function addSkill() {
    form.skills[skills.name] = skills.value
    skills.items?.push({ name: skills.name, value: skills.value })
    skills.name = ''
    skills.value = ''
  }

  function updateSkill(index: number): void {
    const updatedSkill = skills.items && skills.items[index]

    if (updatedSkill) {
      updatedSkill.name = updatedSkill.name.trim()
      updatedSkill.value = updatedSkill.value.trim()
    }
  }

  function deleteSkill(index: number): void {
    skills.items?.splice(index, 1)
  }

  const jsonFormatAttributes = jsonFormat(
    ref<Dictionary[]>(attributes.items || [])
  )
  const jsonFormatSkills = jsonFormat(ref<Dictionary[]>(skills.items || []))

  const create = async () => {
    if (
      !form.name ||
      !form.race ||
      !form.gender ||
      !form.faction ||
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

    const discord_id = authStore.discord_id
    if (!discord_id) {
      error.value = 'Invalid Discord User ID.'
    }

    form.discordID = discord_id

    const jsonFields = ['damage']
    const parsedFields: Partial<NpcCreate> = {}
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

    const npcData: NpcCreate = {
      ...otherFields,
      ...parsedFields,
      attributes: jsonFormatAttributes.value,
      skills: jsonFormatSkills.value
    } as NpcCreate

    isLoading.value = true
    try {
      await npcStore.createNpc(npcData)
    } catch (e) {
      error.value = 'An error occurred while creating the npc.'
    } finally {
      isLoading.value = false
    }
  }

  return {
    addAttribute,
    addSkill,
    attributes,
    create,
    deleteAttribute,
    deleteSkill,
    error,
    factions: Object.values(Faction),
    form,
    genders: Object.values(Gender),
    isLoading,
    races: Object.values(Race),
    skills,
    updateAttribute,
    updateSkill
  }
}
