import type { RouteRecordRaw } from 'vue-router'

import NpcsModule from './Module.vue'
import NpcCreate from './views/Create.vue'
import NpcDetails from './views/View.vue'
import NpcList from './views/List.vue'
import NpcUpdate from './views/Update.vue'

const NpcRoutes: Array<RouteRecordRaw> = [
  {
    path: '/Npcs',
    component: NpcsModule,
    children: [
      {
        path: '',
        name: 'NpcList',
        component: NpcList
      },
      {
        path: 'create',
        name: 'NpcCreate',
        component: NpcCreate,
        props: true
      },
      {
        path: ':id',
        name: 'NpcDetails',
        component: NpcDetails,
        props: true
      },
      {
        path: 'update',
        name: 'NpcUpdate',
        component: NpcUpdate
      }
    ]
  }
]

export default NpcRoutes
