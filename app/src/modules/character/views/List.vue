<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useCharacterStore } from '../character.store'
import CharacterCard from '@/components/CharacterCard.vue'

const characterStore = useCharacterStore()
const characters = ref<
  {
    id: number
    name: string
    race: string
    gender: string
    damage: string | Record<string, any>
  }[]
>([])

onMounted(async () => {
  await characterStore.getCharacters()
  characters.value = characterStore.characters
})
</script>

<template>
  <div>
    <template v-if="characters.length">
      <div class="row">
        <div
          class="col-md-4"
          v-for="character in characters"
          :key="character.id"
        >
          <CharacterCard
            :to="{ name: 'CharacterDetails', params: { id: character.id } }"
            :name="character.name"
            :race="character.race"
            :gender="character.gender"
            :damage="character.damage"
          />
        </div>
      </div>
    </template>
    <p v-else>Loading Characters...</p>
  </div>
</template>
