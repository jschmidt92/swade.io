import { getCurrentInstance, reactive, ref } from 'vue'
import { useEncounterStore } from './encounter.store'
import { EncounterCreate, EncounterData } from './encounter.interfaces'

export function useEncounterData() {
  const form = reactive<EncounterCreate>({
    name: '',
    notes: '',
    body: ''
  })

  const socket = getCurrentInstance()
  const encounterStore = useEncounterStore()
  const error = ref<string | null>(null)
  const isLoading = ref(false)
  const sortedCharacters = ref<any>([])

  socket?.appContext.config.globalProperties.$onSocketEvent('initiativeUpdated', (data: EncounterData) => {
      console.log(data)
      sortCards(data)
    }
  )

  socket?.appContext.config.globalProperties.$onSocketEvent('nextPlayerTurn', () => {
      rotateEntities()
    }
  )

  const sortCards = (data: EncounterData) => {
    const encounter = encounterStore.encounter

    if (encounter) {
      try {
        const initiativeOrder = data.initiative_order || []

        if (!Array.isArray(initiativeOrder)) {
          console.error('Initiative order is not an array:', initiativeOrder)
          return
        }

        const allEntities = [...encounter.characters, ...encounter.npcs]

        const sortedEntities = allEntities
          .filter((entity) => entity.damage?.Inc === 'No' && entity.name)
          .sort((a, b) => {
            const indexA = a.name ? initiativeOrder.indexOf(a.name) : -1
            const indexB = b.name ? initiativeOrder.indexOf(b.name) : -1
            return indexA - indexB
          })

        sortedCharacters.value = sortedEntities

        encounterStore.setCharacterOrder(sortedCharacters.value)
      } catch (error) {
        console.error('Error parsing initiative_order:', error)
      }
    }
  }

  const create = async () => {
    if (!form.name) {
      error.value = 'Please fill in all required fields.'
      return
    }

    const { ...otherFields } = form

    const encounterData: EncounterCreate = {
      ...otherFields
    } as EncounterCreate

    isLoading.value = true
    try {
      await encounterStore.createEncounter(encounterData)
    } catch (e) {
      error.value = 'An error occurred while creating the encounter.'
    } finally {
      isLoading.value = false
    }
  }

  const getFaction = (faction: string) => {
    switch (faction) {
      case 'unknown':
        return 'bg-secondary'
      case 'neutral':
        return 'bg-warning'
      case 'friendly':
        return 'bg-success'
      case 'enemy':
        return 'bg-danger'
      default:
        return 'bg-info'
    }
  }

  const rotateEntities = () => {
    if (sortedCharacters.value.length < 2) {
      return
    }

    const firstEntity = sortedCharacters.value.shift()
    sortedCharacters.value.push(firstEntity)
  }

  return {
    create,
    error,
    form,
    getFaction,
    rotateEntities,
    sortCards
  }
}
