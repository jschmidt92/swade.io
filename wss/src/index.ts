import { createServer, ServerOptions } from 'https'
import { Socket, Server } from 'socket.io'
import { EventsModule } from './modules/events/events.module'
import { MessagesModule } from './modules/messages/messages.module'
import dotenv from 'dotenv'
import fs from 'fs'
import { GamesModule } from './modules/games/games.module'

dotenv.config()

const PORT = process.env.PORT || 3000
const sslOptions: ServerOptions = {
  key: fs.readFileSync('certs/innovativedevsolutions.org-key.pem'),
  cert: fs.readFileSync('certs/innovativedevsolutions.org-cert.pem')
}

const httpsServer = createServer(sslOptions)
const io = new Server(httpsServer, {
  cors: {
    origin: '*',
    methods: ['GET', 'POST'],
    allowedHeaders: '*'
  }
})

new EventsModule(io)
new MessagesModule(io)
new GamesModule(io)

io.on('connection', (socket: Socket) => {
  console.log(`Client connected: ${socket.id}`)

  socket.on('message', (message: string) => {
    console.log('Recieved message:', message)
  })
  socket.on('disconnect', () => {
    console.log(`Client disconnected: ${socket.id}`)
  })
})

httpsServer.listen(PORT, () => {
  console.log(`WebSocket server listening on port ${PORT}`)
})
