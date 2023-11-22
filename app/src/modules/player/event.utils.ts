import { onMounted, ref } from 'vue'
import { useAuthStore } from '@/stores/auth.store'
import { useEventStore } from './event.store'
import { useSocketIO } from '@/plugins/socket.io'
import { EventAttendance } from './event.interfaces'

export const useEventData = () => {
  const authStore = useAuthStore()
  const eventStore = useEventStore()
  const events = ref<
    {
      id: number
      title: string
      date: Date
      details: string
      attendance: Record<string, any>
    }[]
  >([])

  const { socket } = useSocketIO()

  socket.on('attendanceUpdateHandled', (message: string) => {
    console.log(message)
    refreshEvents()
  })

  const handleAttendanceUpdate = async (
    event_id: number,
    attendance: boolean
  ) => {
    await eventStore.updateAttendance({
      event_id: event_id,
      discord_id: authStore.discord_id,
      attendance: attendance
    })
    
    const eventData = {userId: authStore.discord_id, status: attendance}
    socket.emit('attendanceUpdate', eventData)
  }

  const refreshEvents = async () => {
    await eventStore.getUpcomingEvents()
    events.value = eventStore.events
  }

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
    await eventStore.getUpcomingEvents()
    events.value = eventStore.events
    events.value.forEach((item) => {
      const event: EventAttendance = {
        event_id: item.id,
        discord_id: authStore.discord_id
      }
      eventStore.getAttendance(event)
    })
  })

  return {
    countAttendees,
    events,
    formatDate,
    handleAttendanceUpdate,
    totalAttendees,
    refreshEvents
  }
}
