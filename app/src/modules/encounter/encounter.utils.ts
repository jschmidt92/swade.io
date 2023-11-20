import { reactive, ref } from 'vue'
import { useEncounterStore } from './encounter.store'
import { EncounterCreate } from './encounter.interfaces'

export function useEncounterData() {
  const form = reactive<EncounterCreate>({
    name: '',
    notes: '',
    body: ''
  })

  const encounterStore = useEncounterStore()
  const error = ref<string | null>(null)
  const isLoading = ref(false)

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
        return 'bg-secondary'
    }
  }

  return {
    create,
    error,
    form,
    getFaction
  }
}
