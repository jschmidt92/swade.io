<script lang="ts" setup>
import { onMounted } from 'vue'
import { useMonsterStore } from '../monster.store'
import DiceRoller from '@/components/DiceRoller.vue'
import avatar from '@/assets/default.jpg'

const props = defineProps({ id: String })
const monsterStore = useMonsterStore()
const webhook = "https://discord.com/api/webhooks/1128793925461737742/6ecKxmLAYFcNapF_sjA32Uq14zU_ScPIrYEJIftDWYGuUDb7tG4W50pbhmKvofKxVsDW"

const getDamageTypeClass = (key: string) => {
  const damageTypeClasses: Record<string, string> = {
    Inc: 'border-success',
    Wounds: 'border-danger',
    Fatigue: 'border-warning'
  }

  return `d-flex justify-content-center align-items-center border rounded-circle ${damageTypeClasses[key]}`
}

onMounted(async () => {
  await monsterStore.getMonster(props.id)
})
</script>

<template>
  <div v-if="monsterStore.error">{{ monsterStore.error }}</div>
  <div v-else-if="monsterStore.monster" style="padding-bottom: 1em;">
    <div class="row align-items-start">
      <div class="col-md-4">
        <div class="card shadow-sm mb-3" style="max-width: 540px;">
          <div class="row g-0">
            <div class="col-md-4">
              <img :src="avatar" class="img-fluid h-100" alt="...">
            </div>
            <div class="col-md-8">
              <div class="card-header card-title bg-dark-subtle h5">{{ monsterStore.monster.name }}</div>
              <div class="card-body">
                <ul class="list-group text-capitalize">
                  <li class="list-group-item border-0 pt-2 ps-0 pb-0"><span class="fw-semibold">Race: </span>{{ monsterStore.monster.race }}</li>
                  <li class="list-group-item border-0 ps-0 py-0"><span class="fw-semibold">Gender: </span>{{ monsterStore.monster.gender }}</li>
                  <li class="list-group-item border-0 ps-0 py-0"><span class="fw-semibold"> Ammo: </span>{{ monsterStore.monster.ammo }}</li>
                  <li class="list-group-item border-0 ps-0 py-0"><span class="fw-semibold">Money: </span>{{ monsterStore.monster.money }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Primary</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <li class="list-group-item border-0 pt-2 pb-0"><span class="fw-semibold">Charisma: </span>{{ monsterStore.monster.charisma }}</li>
              <li class="list-group-item border-0 py-0"><span class="fw-semibold">Pace: </span>{{ monsterStore.monster.pace }}</li>
              <li class="list-group-item border-0 py-0"><span class="fw-semibold">Parry: </span>{{ monsterStore.monster.parry }}</li>
              <li class="list-group-item border-0 py-0"><span class="fw-semibold">Toughness: </span>{{ monsterStore.monster.toughness }}</li>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Damage</div>
          <div class="card-body">
            <div class="d-flex flex-row justify-content-around align-items-center">
              <div v-for="(value, key) in monsterStore.monster.damage" :key="key" class="d-flex flex-column text-center">
                <div :class="getDamageTypeClass(key as string)" style="width: 55px; height: 55px;">{{ value }}</div>
                <p class="card-text">{{ key }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Skills</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <li class="list-group-item border-0 py-0" v-for="(value, key) in monsterStore.monster.attributes" :key="key"><span class="fw-semibold">{{ key }}: </span>{{ value }}</li>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Skills</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <li class="list-group-item border-0 py-0" v-for="(value, key) in monsterStore.monster.skills" :key="key"><span class="fw-semibold">{{ key }}: </span>{{ value }}</li>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Hindrances</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <li class="list-group-item border-0 fw-semibold py-0" v-for="hindrance in monsterStore.monster.hindrances.split(',')" :key="hindrance">{{ hindrance.trim() }}</li>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Edges</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <li class="list-group-item border-0 fw-semibold py-0" v-for="edge in monsterStore.monster.edges.split(',')" :key="edge">{{ edge.trim() }}</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="col-md-4">
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Cyberware</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <template v-if="monsterStore.monster.cyberware.length > 0">
                <li class="list-group-item border-0 fw-semibold py-0" v-for="cyberware in monsterStore.monster.cyberware" :key="cyberware.id">{{ cyberware.name }}</li>
              </template>
              <template v-else>
                <li class="list-group-item border-0 fw-semibold py-0">None</li>
              </template>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Powers</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <template v-if="monsterStore.monster.powers.length > 0">
                <li class="list-group-item border-0 fw-semibold py-0" v-for="power in monsterStore.monster.powers" :key="power.id">{{ power.name }}</li>
              </template>
              <template v-else>
                <li class="list-group-item border-0 fw-semibold py-0">None</li>
              </template>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Weapons</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <template v-if="monsterStore.monster.weapons.length > 0">
                <li class="list-group-item border-0 py-0" v-for="(weapon, index) in monsterStore.monster.weapons" :key="index">({{ weapon.quantity }}x) <span class="fw-semibold">{{ weapon.weapon.name }}</span></li>
              </template>
              <template v-else>
                <li class="list-group-item border-0 fw-semibold py-0">None</li>
              </template>
            </ul>
          </div>
        </div>
        <div class="card shadow-sm mb-3">
          <div class="card-header card-title bg-dark-subtle h6">Gear</div>
          <div class="card-body">
            <ul class="list-group rounded-0 text-capitalize">
              <template v-if="monsterStore.monster.gear.length > 0">
                <li class="list-group-item border-0 py-0" v-for="(gear, index) in monsterStore.monster.gear" :key="index">({{ gear.quantity }}x) <span class="fw-semibold">{{ gear.gear.name }}</span></li>
              </template>
              <template v-else>
                <li class="list-group-item border-0 fw-semibold py-0">None</li>
              </template>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div v-else>
    <p>Loading Monster...</p>
  </div>
  <DiceRoller :webhook="webhook" />
</template>
