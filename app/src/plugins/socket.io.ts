import { App } from 'vue'
import { io, Socket } from 'socket.io-client'

interface SocketIOPluginOptions {
  connectionUrl: string
}

export const SocketIOPlugin = {
  install: (app: App, options: SocketIOPluginOptions) => {
    const socket: Socket = io(options.connectionUrl)

    app.config.globalProperties.$socket = socket
    app.provide('socket', socket)

    socket.on('connect', () => {
      console.log(`Client with id ${socket.id} connected!`)
    })

    app.config.globalProperties.$emitSocketEvent = (
      eventName: string,
      data: any
    ) => {
      socket.emit(eventName, data)
    }

    app.config.globalProperties.$onSocketEvent = (
      eventName: string,
      callback: (...args: any[]) => void
    ) => {
      socket.on(eventName, callback)
    }

    app.config.globalProperties.$disconnectSocket = () => {
      socket.disconnect()
    }
  }
}

export default SocketIOPlugin
