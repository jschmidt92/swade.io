<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useEncounterStore } from '../encounter.store'

const encounterStore = useEncounterStore()
const encounters = ref<{ id: number; name: string; }[]>([])

onMounted(async () => {
  await encounterStore.getEncounters()
  encounters.value = encounterStore.encounters
})
</script>

<template>
  <div class="col-md-12">
    <template v-if="encounters.length">
      <ul class="list-group row">
        <li class="list-group-item col-md-4 border-light" v-for="encounter in encounters" :key="encounter.id">
          <router-link class="nav-link" :to="{ name: 'EncounterDetails', params: { id: encounter.id} }" :name="encounter.name">{{ encounter.name }}</router-link>
        </li>
      </ul>
    </template>
    <p v-else>Loading Encounters...</p>
  </div>
</template>
