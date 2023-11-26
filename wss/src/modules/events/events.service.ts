import { Server } from 'socket.io'
import { Attendance } from './dtos/event.dto'
import { Initiative } from './dtos/initiative.dto'

export class EventsService {
  constructor(private readonly io: Server) {}

  handleAttendanceUpdate(socket: string, data: Attendance): void {
    console.log(`Attendance update from client ${socket}:`, data)
    this.io.emit('attendanceUpdated', data)
  }
  handleInitiativeUpdate(data: Initiative): void {
    console.log(`Initiative updated:`, data)
    this.io.emit('initiativeUpdated', data)
  }
  handleInitiativeNextTurn(): void {
    console.log("Next player's turn")
    this.io.emit('nextPlayerTurn')
  }
}
