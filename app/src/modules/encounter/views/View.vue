<script lang="ts" setup>
import { computed, onMounted } from 'vue'
import DiceRoller from '@/components/DiceRoller.vue'
import banner from '@/assets/banner.jpg'
import BaseEntityCard from '../components/BaseEntityCard.vue'
import { useEncounterStore } from '../encounter.store'
import { useEncounterData } from '../encounter.utils'

const props = defineProps({ id: String })
const webhook = 'https://discord.com/api/webhooks/1129538520214683739/bYEVm_ar3DwJCqKrWn_pcvbTZleCXxZShbBghL6nkmRajbXiAfmoZljU3R5_silFtAcC'
const encounterStore = useEncounterStore()

const { getFaction, sortedCharacters, sortedNpcs } = useEncounterData()
const combinedEntities = computed(() => {
  return sortedCharacters.value.concat(sortedNpcs.value)
})

onMounted(async () => {
  await encounterStore.getEncounter(props.id)
})
</script>

<template>
  <div v-if="encounterStore.error">{{ encounterStore.error }}</div>
  <div v-else-if="encounterStore.encounter" style="padding-bottom: 1em">
    <div class="row">
      <div class="col-md-6">
        <div class="card shadow-sm">
          <img :src="banner" class="card-img-top" alt="..." />
          <div class="card-header card-title bg-dark-subtle fs-5">
            {{ encounterStore.encounter.name }}
          </div>
          <div class="card-body">
            <p class="card-title text-uppercase fs-6">Notes:</p>
            <p class="card-text small">{{ encounterStore.encounter.notes }}</p>
            <hr />
            <p class="card-title text-uppercase fs-6">
              Events / Triggers / Traps:
            </p>
            <p class="card-text small">{{ encounterStore.encounter.body }}</p>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="row">
          <div class="col-md-12 mb-4">
            <div class="card shadow-sm mb-3">
              <div class="card-header card-title text-uppercase bg-dark-subtle mb-1">
                Initiative List
              </div>
              <div class="card-body">
                <div class="d-flex justify-content-start align-items-center">
                  <span class="me-2">Key:</span>
                  <div>
                    <span class="bg-secondary border-secondary p-1">Unknown</span>
                    <span class="bg-danger border-danger p-1">Enemy</span>
                    <span class="bg-warning border-warning p-1">Neutral</span>
                    <span class="bg-success border-success p-1">Friendly</span>
                    <span class="bg-info border-info p-1">Player</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="card shadow-sm mb-3">
              <div class="card-header card-title text-uppercase bg-dark-subtle border-0">
                In Combat
              </div>
            </div>
            <template v-for="entity in combinedEntities" :key="entity.name">
              <BaseEntityCard
                :name="entity.name"
                :class="entity.type === 'character' ? 'bg-info' : getFaction(entity.faction)"
                :damage="entity.damage"
              />
            </template>
          </div>
          <div class="col-md-6">
            <div class="card shadow-sm mb-3">
              <div class="card-header card-title text-uppercase bg-dark-subtle border-0">
                Out Of Combat
              </div>
            </div>
            <template v-for="character in encounterStore.encounter.characters">
              <template v-if="character.damage.Inc === 'Yes'">
                <BaseEntityCard
                  :name="character.name"
                  class="bg-info"
                  :damage="character.damage"
                />
              </template>
            </template>
            <template v-for="npc in encounterStore.encounter.npcs">
              <template v-if="npc.damage.Inc === 'Yes'">
                <BaseEntityCard
                  :name="npc.name"
                  :class="getFaction(npc.faction)"
                  :damage="npc.damage"
                />
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
