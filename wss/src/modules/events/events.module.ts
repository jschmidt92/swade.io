import { Server } from 'socket.io'
import { EventsGateway } from './events.gateway'

export class EventsModule {
  constructor(private readonly io: Server) {
    this.initializeGateways()
  }

  private initializeGateways() {
    new EventsGateway(this.io)
  }
}
