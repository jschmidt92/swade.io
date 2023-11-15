<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useNpcStore } from '../npc.store.js'
import NpcCard from '@/components/CharacterCard.vue'

const npcStore = useNpcStore()
const npcs = ref<
  {
    id: number
    name: string
    race: string
    gender: string
    damage: string | Record<string, any>
  }[]
>([])

onMounted(async () => {
  await npcStore.getNpcs()
  npcs.value = npcStore.npcs
})
</script>

<template>
  <div>
    <template v-if="npcs.length">
      <div class="row">
        <div class="col-md-4" v-for="npc in npcs" :key="npc.id">
          <NpcCard
            :to="{ name: 'NpcDetails', params: { id: npc.id } }"
            :name="npc.name"
            :race="npc.race"
            :gender="npc.gender"
            :damage="npc.damage"
          />
        </div>
      </div>
    </template>
    <p v-else>Loading NPCs...</p>
  </div>
</template>
../npc.store
