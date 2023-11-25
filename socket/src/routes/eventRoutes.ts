import { Router, Request, Response } from 'express'
import EventController from '../controllers/eventController'

const router = Router()

router.post('/attendanceUpdate', (req: Request, res: Response) => {
  const data = req.body
  const result = EventController.handleAttendanceUpdate(data)
  res.json(result)
})

router.post('/initiativeUpdate', (req: Request, res: Response) => {
  const data = req.body
  const result = EventController.handleInitiativeUpdate(data)
  res.json(result)
})

router.post('/initiativeTurn', (req: Request, res: Response) => {
  const result = EventController.handleInitiativeTurn()
  res.json(result)
})

export default router
