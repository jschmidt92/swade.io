<script lang="ts" setup>
import { onMounted } from 'vue'
import { useEncounterStore } from '../encounter.store'
import DiceRoller from '@/components/DiceRoller.vue'
import banner from '@/assets/banner.jpg'
import BaseEntityCard from '../components/BaseEntityCard.vue';

const props = defineProps({ id: String })
const encounterStore = useEncounterStore()
const webhook = 'https://discord.com/api/webhooks/1129538520214683739/bYEVm_ar3DwJCqKrWn_pcvbTZleCXxZShbBghL6nkmRajbXiAfmoZljU3R5_silFtAcC'

onMounted(async () => {
  await encounterStore.getEncounter(props.id)
})
</script>

<template>
  <div v-if="encounterStore.error">{{ encounterStore.error }}</div>
  <div v-else-if="encounterStore.encounter" style="padding-bottom: 1em;">
    <div class="row">
      <div class="col-md-6">
        <div class="card shadow-sm">
          <img :src="banner" class="card-img-top" alt="...">
          <div class="card-header card-title bg-dark-subtle fs-5">{{ encounterStore.encounter.name }}</div>
          <div class="card-body">
            <p class="card-title text-uppercase fs-6">Notes:</p>
            <p class="card-text small">{{ encounterStore.encounter.notes }}</p>
            <hr>
            <p class="card-title text-uppercase fs-6">Events / Triggers / Traps:</p>
            <p class="card-text small">{{ encounterStore.encounter.body }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="row">
          <div class="col-md-12 mb-4">
            <div class="card shadow-sm">
              <div class="card-header card-title text-uppercase bg-dark-subtle mb-1">Initiative List</div>
              <div class="card-body">
                <div class="d-flex justify-content-start align-items-center">
                  <span class="me-2">Key:</span>
                  <div>
                    <button class="btn btn-sm btn-secondary disabled">Unknown</button>
                    <button class="btn btn-sm btn-danger disabled">Enemy</button>
                    <button class="btn btn-sm btn-warning disabled">Neutral</button>
                    <button class="btn btn-sm btn-success disabled">Friendly</button>
                    <button class="btn btn-sm btn-info disabled">Player</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card shadow-sm mb-3">
              <div class="card-header card-title text-uppercase bg-dark-subtle border-0">In Combat</div>
            </div>
            <template v-for="character in encounterStore.encounter.characters">
              <template v-if="character.damage.Inc === 'No'">
                <BaseEntityCard :name="character.name" class="bg-info" :damage="character.damage"/>
              </template>
            </template>
            <template v-for="monster in encounterStore.encounter.monsters">
              <template v-if="monster.damage.Inc === 'No'">
                <BaseEntityCard :name="monster.name" class="bg-danger" :damage="monster.damage"/>
              </template>
            </template>
          </div>
          <div class="col-md-6">
            <div class="card shadow-sm mb-3">
              <div class="card-header card-title text-uppercase bg-dark-subtle border-0">Out Of Combat</div>
            </div>
            <template v-for="character in encounterStore.encounter.characters">
              <template v-if="character.damage.Inc === 'Yes'">
                <BaseEntityCard :name="character.name" class="bg-info" :damage="character.damage"/>
              </template>
            </template>
            <template v-for="monster in encounterStore.encounter.monsters">
              <template v-if="monster.damage.Inc === 'Yes'">
                <BaseEntityCard :name="monster.name" class="bg-danger" :damage="monster.damage"/>
              </template>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading Encounter...</p>
  </div>
  <DiceRoller :webhook="webhook" />
</template>