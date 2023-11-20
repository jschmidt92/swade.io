interface EventCreate {
  [key: string]: any
  title: string
  date: Date
  details: string
}

interface Event {
  id: number
  title: string
  date: Date
  details: string
  attendance: Record<string, any>
}

interface EventAttendance {
  event_id: number
  discord_id: string
}

interface EventUpdateAttendance {
  event_id: number
  discord_id: string
  attendance: boolean
}

export type { Event, EventAttendance, EventCreate, EventUpdateAttendance }
