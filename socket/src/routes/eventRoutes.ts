// src/routes/eventRoutes.ts
import { Router, Request, Response } from 'express'
import EventController from '../controllers/eventController'

const router = Router()

// Route for handling attendance updates
router.post('/attendanceUpdate', (req: Request, res: Response) => {
  const eventData = req.body
  const result = EventController.handleAttendanceUpdate(eventData)
  res.json(result)
})

// Route for handling item transactions (buy/sell)
router.post('/itemTransaction', (req: Request, res: Response) => {
  const eventData = req.body
  const result = EventController.handleItemTransaction(eventData)
  res.json(result)
})

// Route for handling received payments
router.post('/paymentReceived', (req: Request, res: Response) => {
  const eventData = req.body
  const result = EventController.handlePaymentReceived(eventData)
  res.json(result)
})

// Route for handling damage taken
router.post('/damageTaken', (req: Request, res: Response) => {
  const eventData = req.body
  const result = EventController.handleDamageTaken(eventData)
  res.json(result)
})

export default router
