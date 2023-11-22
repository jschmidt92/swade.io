import { io } from 'socket.io-client'

export const useSocketIO = () => {
    const socket = io('https://websocket.innovativedevsolutions.org')
    return { socket }
}
