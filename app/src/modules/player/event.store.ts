import { defineStore } from 'pinia'
import {
  Event,
  EventAttendance,
  EventCreate,
  EventUpdateAttendance
} from './event.interfaces'

const BASE_URL = 'https://apiv1.innovativedevsolutions.org'

export const useEventStore = defineStore('player', {
  state: () => ({
    event: null as Event | null,
    events: [] as Event[],
    error: null as string | null
  }),
  actions: {
    async getEventById(id: number) {
      try {
        let data = await fetch(`${BASE_URL}/events/${id}/`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.event = await data.json()
        return this.event
      } catch (err: any) {
        this.error = err.message
        console.log(this.error)
      }
    },
    async getUpcomingEvents() {
      try {
        let data = await fetch(`${BASE_URL}/events/?limit=3&sort=-date`)
        if (!data.ok) {
          throw Error('No data available')
        }
        this.events = await data.json()
        this.events.sort(
          (a, b) => new Date(a.date).getTime() - new Date(b.date).getTime()
        )
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
        const index = this.events.findIndex((e) => e.id === updatedEvent.id)
        if (index !== -1) {
          this.events.splice(index, 1, updatedEvent)
        }
      } catch (err: any) {
        this.error = err.message
        console.error(this.error)
      }
    },
    async getAttendance(event: EventAttendance) {
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
