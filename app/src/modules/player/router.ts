import type { RouteRecordRaw } from 'vue-router'

import PlayersModule from './Module.vue'
import PlayerDashboard from './views/Dashboard.vue'
import PlayerInventory from './views/Inventory.vue'

const playerRoutes: Array<RouteRecordRaw> = [
  {
    path: '/player',
    component: PlayersModule,
    children: [
      {
        path: ':id/dashboard',
        name: 'PlayerDashboard',
        component: PlayerDashboard
      },
      {
        path: ':id/inventory',
        name: 'PlayerInventory',
        component: PlayerInventory
      }
    ]
  }
]

export default playerRoutes
