import { Server, Socket } from 'socket.io'
import { Attendance } from './dtos/event.dto'
import { EventsService } from './events.service'
import { Initiative } from './dtos/initiative.dto'

export class EventsGateway {
  private readonly eventsService: EventsService

  constructor(private readonly io: Server) {
    this.eventsService = new EventsService(io)
    this.handleEvents()
  }

  private handleEvents() {
    this.io.on('connection', (socket: Socket) => {
      socket.on('attendanceUpdate', (data: Attendance) => {
        this.eventsService.handleAttendanceUpdate(socket.id, data)
      })
      socket.on('initiativeUpdate', (data: Initiative) => {
        this.eventsService.handleInitiativeUpdate(data)
      })
      socket.on('initiativeNextTurn', () => {
        this.eventsService.handleInitiativeNextTurn()
      })
    })
  }
}
