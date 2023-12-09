import { Server } from 'socket.io'
import { GamesGateway } from './games.gateway'

export class GamesModule {
  constructor(private readonly io: Server) {
    this.initializeGateways()
  }

  private initializeGateways() {
    new GamesGateway(this.io)
  }
}
