import express, { Request, Response } from 'express'
import fs from 'fs'
import { Server, Socket } from 'socket.io'
import { createServer } from 'https'

import eventRoutes from './routes/eventRoutes'
import SocketManager from './sockets/socketManager'

const app = express()
const port = process.env.PORT || 3000

const wssOptions = {
  key: fs.readFileSync('certificates/innovativedevsolutions.org-key.pem'),
  cert: fs.readFileSync('certificates/innovativedevsolutions.org-cert.pem')
}

const wss = createServer(wssOptions, app)

const io = new Server(wss, {
  cors: { origin: '*', methods: ['GET', 'POST'], allowedHeaders: '*' }
})

app.use('/events', eventRoutes)

new SocketManager(io)

app.get('/', (req: Request, res: Response) => {
  res.send({ message: 'Welcome to Socket.IO over WSS!' })
})

io.on('connection', (socket: Socket) => {
  console.log('Client connected', socket.id)

  socket.on('message', (message: string) => {
    JSON.stringify(message)
    console.log(`Received message:`, message)
  })

  socket.on('disconnect', () => {
    console.log('Client disconnected', socket.id)
  })
})

wss.listen(port, () => {
  console.log(`Socket.IO server listening on port ${port}`)
})
