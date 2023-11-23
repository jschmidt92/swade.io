import { getCurrentInstance, onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { useEventStore } from './event.store'
import { Event, EventAttendance } from './event.interfaces'

export const useEventData = () => {
  const socket = getCurrentInstance()
  const authStore = useAuthStore()
  const eventStore = useEventStore()
  const events = ref<Event[]>([])

  socket?.appContext.config.globalProperties.$onSocketEvent(
    'attendanceUpdateHandled',
    (message: string) => {
      console.log(message)
      refreshEvents()
    }
  )

  const handleAttendanceUpdate = async (
    event_id: number,
    attendance: boolean
  ) => {
    await eventStore.updateAttendance({
      event_id: event_id,
      discord_id: authStore.discord_id,
      attendance: attendance
    })

    const eventData = {
      event_id: event_id,
      discord_id: authStore.discord_id,
      status: attendance
    }
    socket?.appContext.config.globalProperties.$emitSocketEvent(
      'attendanceUpdate',
      eventData
    )
  }

  const refreshEvents = async () => {
    await eventStore.getUpcomingEvents()

    events.value = eventStore.events.map((eventItem: Event) => ({
      ...eventItem,
      attending: countAttendees(eventItem.attendance),
      total_players: totalAttendees(eventItem.attendance)
    }))

    events.value.forEach((event) => {
      const eventAttendance: EventAttendance = {
        event_id: event.id,
        discord_id: authStore.discord_id
      }
      eventStore.getAttendance(eventAttendance)
    })
  }

  const countAttendees = (attendance: Record<string, boolean>): number => {
    return Object.values(attendance).filter((value) => value === true).length
  }

  const totalAttendees = (attendance: Record<string, any>): number => {
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
    await refreshEvents()
  })

  return {
    countAttendees,
    events,
    formatDate,
    handleAttendanceUpdate,
    totalAttendees
  }
}
