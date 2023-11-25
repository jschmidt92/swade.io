import { Server, Socket } from 'socket.io'
import EventController from '../controllers/eventController'
import { Attendance } from '../interfaces/attendance.interface'

class SocketManager {
  private io: Server

  constructor(io: Server) {
    this.io = io
    this.setupEventListeners()
  }

  private setupEventListeners() {
    this.io.on('connection', (socket: Socket) => {
      socket.on('attendanceUpdate', (data: Attendance) => {
          const message = EventController.handleAttendanceUpdate(data)

          console.log('Attendance Update Handled')

          this.io.emit('attendanceUpdateHandled', message)
        }
      )

      socket.on('initiativeDealt', (data: string) => {
        const message = EventController.handleInitiativeUpdate(data)

        console.log('Initiative Update Handled')

        this.io.emit('initiativeUpdateHandled', message)
      })

      socket.on('initiativeNextTurn', () => {
        console.log('Initiative Turn Handled')

        this.io.emit('initiativeTurnHandled')
      })
    })
  }
}

export default SocketManager
