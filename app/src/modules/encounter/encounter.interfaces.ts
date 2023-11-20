interface EncounterCreate {
  [key: string]: any
  name: string
  notes: string
  body: string
}

interface EncountersList {
  id: number
  name: string
}

interface EncounterUpdate {
  id?: number
  name?: string
  notes?: string
  body?: string
}

interface EncounterView {
  name: string
  notes: string
  body: string
  characters: any[]
  npcs: any[]
}

export type { EncounterCreate, EncountersList, EncounterUpdate, EncounterView }
