import express, { Request, Response } from 'express'
import { Server, Socket } from 'socket.io'
import fs from 'fs'
import https from 'https' // Import the 'http' module

import eventRoutes from './routes/eventRoutes' // Import your eventRoutes
import SocketManager from './sockets/socketManager' // Import your SocketManager

const app = express()
const port = process.env.PORT || 3000

// Create an HTTP server using the express app
const server = https.createServer({
  key: fs.readFileSync('./certificates/innovativedevsolutions.org-key.pem'),
  cert: fs.readFileSync('./certificates/innovativedevsolutions.org-cert.pem')
}, app)

const io = new Server(server, {
  cors: { origin: '*', methods: ['GET', 'POST'], allowedHeaders: '*' }
})

// Use the eventRoutes for handling events over HTTP
app.use('/events', eventRoutes)

// Initialize the SocketManager with the Socket.IO server
new SocketManager(io)

// Basic route for the home page
app.get('/', (req: Request, res: Response) => {
  res.send({ message: 'Welcome to Swade Socket.IO!' })
})

// Set up a basic socket connection handling
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

// Start the server
server.listen(port, () => {
  console.log(`⚡️ [server]: is listening on port ${port}`)
})
