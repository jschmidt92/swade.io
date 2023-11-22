// src/sockets/socketManager.ts
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
      // Example: Handle 'attendanceUpdate' event from the client
      socket.on(
        'attendanceUpdate',
        (eventData: { userId: string; status: string }) => {
          const result = EventController.handleAttendanceUpdate(eventData)
          socket.emit('attendanceUpdateHandled', result)
        }
      )

      // Example: Handle 'itemTransaction' event from the client
      socket.on(
        'itemTransaction',
        (eventData: { userId: string; action: string; item: string }) => {
          const result = EventController.handleItemTransaction(eventData)
          socket.emit('itemTransactionHandled', result)
        }
      )

      // Example: Handle 'paymentReceived' event from the client
      socket.on(
        'paymentReceived',
        (eventData: { userId: string; amount: number }) => {
          const result = EventController.handlePaymentReceived(eventData)
          socket.emit('paymentReceivedHandled', result)
        }
      )

      // Example: Handle 'damageTaken' event from the client
      socket.on(
        'damageTaken',
        (eventData: { userId: string; damageAmount: number }) => {
          const result = EventController.handleDamageTaken(eventData)
          socket.emit('damageTakenHandled', result)
        }
      )

      // You can add more event listeners here based on your application's needs
    })
  }
}

export default SocketManager
