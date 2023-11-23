import express, { Request, Response } from 'express'
import { Server, Socket } from 'socket.io'
import http from 'http'

import eventRoutes from './routes/eventRoutes'
import SocketManager from './sockets/socketManager'

const app = express()
const port = process.env.PORT || 3000
const server = http.createServer(app)

const io = new Server(server, {
  cors: { origin: '*', methods: ['GET', 'POST'], allowedHeaders: '*' }
})

app.use('/events', eventRoutes)

new SocketManager(io)

app.get('/', (req: Request, res: Response) => {
  res.send({ message: 'Welcome to Swade Socket.IO!' })
})

io.on('connection', (socket: Socket) => {
  console.log('Client connected', socket.id)
  socket.send(`Welcome to Swade Socket.IO!`)

  socket.on('message', (message: string) => {
    console.log(`Received message: ${message}`)
  })

  socket.on('disconnect', () => {
    console.log('Client disconnected', socket.id)
  })
})

server.listen(port, () => {
  console.log(`⚡️ [server]: is listening on port ${port}`)
})
