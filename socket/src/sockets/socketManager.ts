import { Server, Socket } from 'socket.io'
import EventController from '../controllers/eventController'

class SocketManager {
  private io: Server

  constructor(io: Server) {
    this.io = io
    this.setupEventListeners()
  }

  private setupEventListeners() {
    this.io.on('connection', (socket: Socket) => {
      socket.on(
        'attendanceUpdate',
        (eventData: { event_id: string; discord_id: string; status: string }) => {
          const result = EventController.handleAttendanceUpdate(eventData)
          this.io.emit('attendanceUpdateHandled', result)
        }
      )

      socket.on(
        'itemTransaction',
        (eventData: { userId: string; action: string; item: string }) => {
          const result = EventController.handleItemTransaction(eventData)
          socket.emit('itemTransactionHandled', result)
        }
      )

      socket.on(
        'paymentReceived',
        (eventData: { userId: string; amount: number }) => {
          const result = EventController.handlePaymentReceived(eventData)
          socket.emit('paymentReceivedHandled', result)
        }
      )

      socket.on(
        'damageTaken',
        (eventData: { userId: string; damageAmount: number }) => {
          const result = EventController.handleDamageTaken(eventData)
          socket.emit('damageTakenHandled', result)
        }
      )
    })
  }
}

export default SocketManager
