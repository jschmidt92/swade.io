<script lang="ts" setup>
import { usePlayerData } from '../player.utils.js'

const { getPlayerWealth } = usePlayerData()
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">Player Wealth</div>
    <div class="card-body">
      <div class="text-center">
        <p class="card-text mb-0">${{ getPlayerWealth() }}</p>
        <p class="card-text">Credits</p>
      </div>
    </div>
    <div class="card-footer bg-dark-subtle">
      <p class="my-0">Wealth Log</p>
      <div class="d-flex justify-content-between">
        <p class="mb-0 pb-0">October 16, 2023 at 21:00 PM</p>
        <p class="small mb-0 pb-0">
          Player's wealth was adjusted (3,500) credits with note: Paycheck
        </p>
      </div>
    </div>
  </div>
</template>
../player.utils.js