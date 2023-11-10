<script lang="ts" setup>
import DamageCard from './BaseDamgeCom.vue'

defineProps<{ name: string, class: string, damage: { Inc: string; Wounds: string; Fatigue: string; }}>()
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title text-dark h6 border-0 shadow-sm" :class="class">{{ name }}</div>
    <div class="card-body">
        <div class="d-flex flex-row justify-content-around align-items-center">
            <DamageCard type="Inc" :value="damage.Inc" label="Incaped" />
            <DamageCard type="Wounds" :value="damage.Wounds" label="Wounds" />
            <DamageCard type="Fatigue" :value="damage.Fatigue" label="Fatigue" />
        </div>
    </div>
  </div>
</template>
