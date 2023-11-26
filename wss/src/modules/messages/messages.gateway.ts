import { Server, Socket } from 'socket.io'
import { MessagesService } from './messages.service'

export class MessagesGateway {
  private readonly messagesService: MessagesService

  constructor(private readonly io: Server) {
    this.messagesService = new MessagesService(io)
    this.handleMessages()
  }

  private handleMessages() {
    this.io.on('connection', (socket: Socket) => {})
  }
}
