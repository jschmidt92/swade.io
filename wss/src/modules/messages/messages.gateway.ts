import { Server, Socket } from 'socket.io'
import { MessagesService } from './messages.service'
import { CreateMessageDto } from './dtos/message.dto'

export class MessagesGateway {
  private readonly messagesService: MessagesService

  constructor(private readonly io: Server) {
    this.messagesService = new MessagesService(io)
    this.handleMessages()
  }

  private handleMessages() {
    this.io.on('connection', (socket: Socket) => {
      socket.on('createMessage', async (createMessageDto: CreateMessageDto) => {
        const message = await this.messagesService.create(createMessageDto)
        this.io.emit('message', message)
        return message
      })
      socket.on('findAllMessages', () => {
        return this.messagesService.findAll()
      })
      socket.on('isTyping', async (isTyping: boolean) => {
        socket.broadcast.emit('typing', { isTyping })
      })
    })
  }
}
