<script lang="ts" setup>
import { onMounted } from 'vue'
import { useCharacterStore } from '@/modules/character/character.store.js'
import avatar from '@/assets/default.jpg'

const props = defineProps({ id: String })
const characterStore = useCharacterStore()

onMounted(async () => {
  await characterStore.getCharacter(props.id)
})
</script>

<template>
  <div v-if="characterStore.error">{{ characterStore.error }}</div>
  <div v-else-if="characterStore.character" style="padding-bottom: 1em">
    <div class="row align-items-start">
      <div class="col-md-4">
        <div class="card shadow-sm mb-3" style="max-width: 540px">
          <div class="row g-0">
            <div class="col-md-4">
              <img :src="avatar" class="img-fluid h-100" alt="..." />
            </div>
            <div class="col-md-8">
              <div class="card-header card-title bg-dark-subtle h5">
                {{ characterStore.character.name }}
              </div>
              <div class="card-body"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4"></div>
    </div>
  </div>
  <div v-else>
    <p>Loading Character...</p>
  </div>
</template>
../player.store.js
