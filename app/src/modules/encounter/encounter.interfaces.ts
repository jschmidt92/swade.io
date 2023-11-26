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
  initiative_order?: string[]
}

interface EncounterData {
  encounter_id: number;
  initiative_order: string[];
}

interface EncounterEntity {
  name: string
  damage: { Inc: string, Wounds: number, Fatigue: number }
  faction: any
  type: string
}

export type { EncounterCreate, EncounterData, EncounterEntity, EncountersList, EncounterUpdate, EncounterView }
