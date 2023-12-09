import { Server } from 'socket.io'
import { CreateMessageDto } from './dtos/message.dto'
import { Message } from './entities/message.entity'

export class MessagesService {
  constructor(private readonly io: Server) {}

  messages: Message[] = []

  create(createMessageDto: CreateMessageDto) {
    const message = { ...createMessageDto }

    this.messages.push(message)

    return message
  }
  findAll() {
    this.io.emit('fetchedMessages', this.messages)
    return this.messages
  }
}
