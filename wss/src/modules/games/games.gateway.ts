import { Server, Socket } from 'socket.io'
import { GamesService } from './games.service'
import { IGameParams } from './dtos/game.dto'

export class GamesGateway {
  private readonly gamesService: GamesService

  constructor(private readonly io: Server) {
    this.gamesService = new GamesService(io)
    this.handleGames()
  }

  private handleGames() {
    this.io.on('connection', (socket: Socket) => {
      socket.on('create-game', () => {
        this.gamesService.createGame()
      })
      socket.on('join-game', ({ gameId, peerId }: IGameParams) => {
        this.gamesService.joinGame({ gameId, peerId }, socket)
      })
    })
  }
}
