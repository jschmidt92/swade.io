<script setup lang="ts">
import BaseInput from '@/components/BaseInput.vue'
import BaseTextBox from '@/components/BaseTextBox.vue'
import { useEncounterData } from '../encounter.utils'

const { create, error, form } = useEncounterData()
</script>

<template>
  <div class="col-md-6 offset-md-3">
    <form class="mb-3" @submit.prevent="create">
      <BaseInput
        v-model="form.name"
        label="Encounter Name:"
        type="text"
        class="mb-3"
      />
      <BaseInput v-model="form.notes" label="Notes:" type="text" class="mb-3" />
      <BaseTextBox
        v-model="form.body"
        label="Events / Triggers / Traps"
        type="text"
        class="mb-3 h-100"
      />

      <div class="d-grid gap-2">
        <button type="submit" class="btn btn-outline-success rounded-0">
          Create
        </button>
      </div>
      <p v-if="error">{{ error }}</p>
    </form>
  </div>
</template>
