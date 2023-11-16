import { ComputedRef, computed, reactive, ref, Ref } from 'vue'
import { useNpcStore, type NpcCreate } from './npc.store'

interface Dictionary {
  name: string
  value: string
}

interface FormNpcCreate
  extends Omit<NpcCreate, 'attributes' | 'skills' | 'damage'> {
  attributes: Record<string, string>
  skills: Record<string, string>
  damage: string
}

export function useNpcData() {
  const form = reactive<FormNpcCreate>({
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

  const npcStore = useNpcStore()
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

  const factions = [
    { label: 'Unknown', value: 'unknown' },
    { label: 'Neutral', value: 'neutral' },
    { label: 'Friendly', value: 'friendly' },
    { label: 'Enemy', value: 'enemy' }
  ]

  const races = [
    { label: 'Android', value: 'android' },
    { label: 'Anklebiter', value: 'anklebiter' },
    { label: 'Angler', value: 'angler' },
    { label: 'A-Pex', value: 'apex' },
    { label: 'Aquarian', value: 'aquarian' },
    { label: 'Aurax', value: 'aurax' },
    { label: 'Avion', value: 'avion' },
    { label: 'Behemoth', value: 'behemoth' },
    { label: 'Bloodwing', value: 'bloodwing' },
    { label: 'Boomer', value: 'boomer' },
    { label: 'Colemata', value: 'colemata' },
    { label: 'Construct', value: 'construct' },
    { label: 'Deader', value: 'deader' },
    { label: 'Death Crawler (Swarm)', value: 'deathcrawler' },
    { label: 'Drake', value: 'drake' },
    { label: 'Dwarf', value: 'dwarf' },
    { label: 'Elf', value: 'elf' },
    { label: 'Floran', value: 'floran' },
    { label: 'Half-Elve', value: 'halfelve' },
    { label: 'Half-Folk', value: 'halffolk' },
    { label: 'Human', value: 'human' },
    { label: 'Hunter', value: 'hunter' },
    { label: 'Insectoid', value: 'insectoid' },
    { label: 'Kalian', value: 'kalian' },
    { label: 'Krok', value: 'krok' },
    { label: 'Krok, Giant', value: 'krokgiant' },
    { label: 'Lightning Darter (Swarm)', value: 'lightningdarter' },
    { label: 'Lacerauns', value: 'lacerauns' },
    { label: 'Mauler', value: 'mauler' },
    { label: 'Rakashan', value: 'rakashan' },
    { label: 'Ravager', value: 'ravager' },
    { label: 'Robot', value: 'robot' },
    { label: 'Sailfin', value: 'sailfin' },
    { label: 'Saurian', value: 'saurian' },
    { label: 'Scrat', value: 'scrat' },
    { label: 'Scute Boar', value: 'scuteboar' },
    { label: 'Serran', value: 'serran' },
    { label: 'Scylla', value: 'scylla' },
    { label: 'Scylla, Giant', value: 'scyllagiant' },
    { label: 'Siren Creeper', value: 'sirencreeper' },
    { label: 'Spitter', value: 'spitter' },
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
    attribute,
    create,
    deleteAttribute,
    deleteSkill,
    error,
    factions,
    form,
    genders,
    isLoading,
    races,
    skill,
    updateAttribute,
    updateSkill
  }
}
