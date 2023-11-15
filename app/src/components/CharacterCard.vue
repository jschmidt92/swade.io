<script setup lang="ts">
import { computed } from 'vue'
import avatar from '@/assets/default.jpg'

const props = defineProps<{
  to: any
  name: string
  race: string
  gender: string
  damage: string | Record<string, any>
}>()

const isCharacterWithoutDamage = computed(() => {
  const damage = props.damage
  if (typeof damage === 'object') {
    return damage.Inc === 'No'
  }
  return false
})
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="row g-0">
      <div class="col-md-4 position-relative">
        <img :src="avatar" class="img-fluid h-100" alt="Character Avatar" />
        <span
          class="badge bg-success position-absolute top-0 end-0 m-2"
          v-if="isCharacterWithoutDamage"
          >Alive</span
        >
      </div>
      <div class="col-md-8 position-relative">
        <div class="card-header card-title bg-dark-subtle h5">{{ name }}</div>
        <div class="card-body">
          <ul class="list-group text-capitalize">
            <li class="list-group-item border-0 pt-2 ps-0 pb-0">
              <span class="fw-semibold">Race: </span>{{ race }}
            </li>
            <li class="list-group-item border-0 pt-2 ps-0 pb-0">
              <span class="fw-semibold">Gender: </span>{{ gender }}
            </li>
          </ul>
          <div class="position-absolute bottom-0 end-0 m-2">
            <div class="btn-group">
              <RouterLink class="btn btn-light" :to="to">View</RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
