<script lang="ts" setup>
import { usePlayerData } from '../player.utils.js'

const { getCurrentDateTime, getPlayerInventory } = usePlayerData()
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">
      Player Inventory
    </div>
    <div class="card-body">
      <div class="table-responsive">
        <table
          class="table table-sm table-dark table-bordered border-light table-striped align-middle"
        >
          <thead>
            <tr>
              <td scope="col" class="col-4">Item</td>
              <td scope="col" class="col-4 text-center">Quantity</td>
              <td scope="col" class="col-4 text-end">Updated</td>
            </tr>
          </thead>
          <tbody>
            <template v-if="getPlayerInventory().length === 0">
              <tr>
                <td colspan="3" class="text-center">
                  You don't have any gear or weapons.
                </td>
              </tr>
            </template>
            <template v-else>
              <tr v-for="(item, index) in getPlayerInventory()" :key="index">
                <td>{{ item.name }}</td>
                <td class="text-center">{{ item.quantity }}</td>
                <td class="text-end">{{ getCurrentDateTime() }}</td>
              </tr>
            </template>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
