import { Server } from 'socket.io'
import { MessagesGateway } from './messages.gateway'

export class MessagesModule {
  constructor(private readonly io: Server) {
    this.initializeGateways()
  }

  private initializeGateways() {
    new MessagesGateway(this.io)
  }
}
