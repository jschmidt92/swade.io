<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useMonsterStore } from '../monster.store'
import MonsterCard from '@/components/CharacterCard.vue';

const monsterStore = useMonsterStore()
const monsters = ref<{ id: number; name: string; race: string, gender: string, damage: string | Record<string, any> }[]>([])

onMounted(async () => {
  await monsterStore.getMonsters()
  monsters.value = monsterStore.monsters
})
</script>

<template>
  <div>
    <template v-if="monsters.length">
      <div class="row">
        <div class="col-md-4" v-for="monster in monsters" :key="monster.id">
          <MonsterCard :to="{ name: 'MonsterDetails', params: { id: monster.id} }" :name="monster.name" :race="monster.race" :gender="monster.gender" :damage="monster.damage" />
        </div>
      </div>
    </template>
    <p v-else>Loading NPCs...</p>
  </div>
</template>
