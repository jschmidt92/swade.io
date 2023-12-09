import dotenv from 'dotenv'
import { PeerServer } from 'peer'

dotenv.config()

const PORT = Number(process.env.PORT)

PeerServer({
  path: '/',
  port: PORT || 3001
})

console.log(`Peer server listening on port: ${PORT}`)
