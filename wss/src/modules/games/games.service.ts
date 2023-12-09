import { Server, Socket } from 'socket.io'
import { v4 as uuidV4 } from 'uuid'
import { IGameParams } from './dtos/game.dto'

const games: Record<string, string[]> = {}

export class GamesService {
  constructor(private readonly io: Server) {}

  createGame() {
    const gameId = uuidV4()
    games[gameId] = []

    console.log(`Client created game ${gameId}`)

    this.io.emit('game-created', { gameId })
  }

  joinGame({ gameId, peerId }: IGameParams, socket: Socket) {
    if (games[gameId]) {
      if (!games[gameId].includes(peerId)) {
        console.log(`Client ${peerId} joined game ${gameId}`)

        games[gameId].push(peerId)
        socket.join(gameId)
        socket.to(gameId).emit('user-joined', { peerId })
      }

      socket.emit('get-users', {
        gameId,
        participants: games[gameId]
      })
    }

    socket.on('disconnect', () => {
      console.log('Client left game', peerId)
      this.leaveGame({ gameId, peerId })
    })
  }

  leaveGame({ gameId, peerId }: { gameId: string; peerId: string }) {
    if (games[gameId]) {
      games[gameId] = games[gameId].filter((id) => id !== peerId)
    } else {
      console.error(`Game with ID ${gameId} does not exist`)
    }
  }
}
