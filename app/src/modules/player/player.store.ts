import { defineStore } from 'pinia'

export interface EventCreate {
  [key: string]: any
  title: string
  date: Date
  details: string
}

export interface Event {
  id: number
  title: string
  date: Date
  details: string
  attendance: Record<string, any>
}

export interface EventAttendance {
  event_id: number
  discord_id: string
}

export interface EventUpdateAttendance {
  event_id: number
  discord_id: string
  attendance: boolean
}

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'
// const BASE_URL = 'http://swade.api:4000'

export const usePlayerStore = defineStore('player', {
  state: () => ({
    event: null as Event | null,
    events: [] as Event[],
    error: null as string | null
  }),
  actions: {
    async getUpcomingEvents() {
      try {
        let data = await fetch(`${BASE_URL}/events/?limit=3&sort=-date`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.events = await data.json()
        this.events.sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime())
        return this.events
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async createEvent(event: EventCreate) {
      try {
        const response = await fetch(`${BASE_URL}/events/new/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(event)
        })
        if (!response.ok) {
          throw Error('Could not create event')
        }
        const newEvent = await response.json()
        this.events.push(newEvent)
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async updateAttendance(event: EventUpdateAttendance) {
      try {
        const response = await fetch(`${BASE_URL}/events/attendance/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(event)
        })
        if (!response.ok) {
          throw Error('Could not update attendance')
        }
        const updatedEvent = await response.json()
        const index = this.events.findIndex(
          (e) => e.id === updatedEvent.id
        )
        if (index !== -1) {
          this.events.splice(index, 1, updatedEvent)
        }
      } catch (err: any) {
        this.error = err.message
        console.error(this.error)
      }
    },
    async getPlayerAttendance(event: EventAttendance) {
      try {
        const response = await fetch(`${BASE_URL}/events/attendance/get/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(event)
        })
        if (!response.ok) {
          throw Error('No data available')
        }
        this.event = await response.json()
      } catch (err: any) {
        this.error = err.message
        console.error(this.error)
      }
    }
  }
})
