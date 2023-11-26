import { Server } from 'socket.io'

export class MessagesService {
  constructor(private readonly io: Server) {}
}
