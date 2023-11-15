<script lang="ts" setup>
import PlayerCharacters from '@/modules/player/components/Characters.vue'
import PlayerEvents from '@/modules/player/components/Events.vue'
import PlayerInventory from '@/modules/player/components/Inventory.vue'
import PlayerLinks from '@/modules/player/components/Links.vue'
import PlayerNotes from '@/modules/player/components/Notes.vue'
// import PlayerProperties from '@/modules/player/components/Properties.vue'
import PlayerWealth from '@/modules/player/components/Wealth.vue'
</script>

<template>
  <div class="row align-items-start">
    <div class="col-md-8">
      <PlayerWealth />
      <PlayerInventory />
      <PlayerEvents />
    </div>
    <div class="col-md-4">
      <PlayerCharacters />
      <!-- <PlayerProperties /> -->
      <PlayerNotes />
      <PlayerLinks />
    </div>
  </div>
</template>
