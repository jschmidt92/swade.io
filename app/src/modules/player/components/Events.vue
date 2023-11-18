<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { usePlayerStore, EventAttendance } from '../player.store'

const playerStore = usePlayerStore()
const authStore = useAuthStore()
const events = ref<
  {
    id: number
    title: string
    date: Date
    details: string
    attendance: Record<string, any>
  }[]
>([])

const countAttendees = (attendance: Record<string, any>) => {
  return Object.values(attendance).filter((value) => value === true).length
}

const totalAttendees = (attendance: Record<string, any>) => {
  return Object.keys(attendance).length
}

const formatDate = (date: any): string => {
  const isoDate = new Date(date)
  const options: Intl.DateTimeFormatOptions = {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
    hour: 'numeric',
    minute: 'numeric',
    timeZoneName: 'short'
  }
  return isoDate.toLocaleString('en-US', options)
}

onMounted(async () => {
  await playerStore.getUpcomingEvents()
  events.value = playerStore.events
  events.value.forEach((item) => {
    const event: EventAttendance = {
      event_id: item.id,
      discord_id: authStore.discord_id
    }
    playerStore.getPlayerAttendance(event)
  })
  events.value.sort((a, b) => a.id = b.id)
})
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">
      Upcomming Events
    </div>
    <div class="card-body">
      <div class="table-responsive">
        <table class="table table-sm border-light table-dark align-middle">
          <thead>
            <tr>
              <td scope="col" class="col-3">Confirmed</td>
              <td scope="col" class="col-6">Event Details</td>
              <td scope="col" class="col-3 text-center">Your Attendance</td>
            </tr>
          </thead>
          <tbody>
            <tr v-for="event in events" :key="event.id">
              <td>{{ countAttendees(event.attendance) }} of {{ totalAttendees(event.attendance) }}</td>
              <td>
                <router-link
                  class="link-info link-underline-opacity-0"
                  to=""
                  >{{ event.title }}</router-link
                >
                <p class="small mb-0">{{ formatDate(event.date) }}</p>
                <p class="small">{{ event.details }}</p>
              </td>
              <td class="text-center">{{ event.attendance[authStore.discord_id] ? 'Yes' : 'No' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
