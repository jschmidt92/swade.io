import { Attendance } from "../interfaces/attendance.interface"

class EventController {
  handleAttendanceUpdate(data: Attendance) {
    const isAttending = data.status === true
    const attendance = isAttending ? 'Attending' : 'Not Attending'

    console.log(
      `User ${data.discord_id} updated attendance status to ${attendance} for ${data.event_id}`
    )

    return { message: 'Attendance updated successfully' }
  }

  handleInitiativeUpdate(data: string) {
    return data
  }

  handleInitiativeTurn() {
    return { message: 'Next turn'}
  }
}

export default new EventController()
