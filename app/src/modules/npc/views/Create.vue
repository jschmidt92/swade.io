<script setup lang="ts">
import BaseInput from '@/components/BaseInput.vue'
import BaseListBox from '@/components/BaseListBox.vue'
import { useNpcData } from '../npc.utils'
import { Gender, Faction, Race } from '../npc.interfaces'
import { convertEnumToArray } from '../npc.utils'

const genders = convertEnumToArray(Gender)
const factions = convertEnumToArray(Faction)
const races = convertEnumToArray(Race)
const {
  addAttribute,
  addSkill,
  attributes,
  create,
  deleteAttribute,
  deleteSkill,
  error,
  form,
  skills,
  updateAttribute,
  updateSkill
} = useNpcData()
</script>

<template>
  <div class="col-md-6 offset-md-3">
    <form class="mb-3" @submit.prevent="create">
      <BaseInput
        v-model="form.discordID"
        label="Discord User ID:"
        type="text"
        class="mb-3"
        disabled
        hidden
      />
      <BaseInput
        v-model="form.name"
        label="Npc Name:"
        type="text"
        class="mb-3"
      />
      <BaseListBox v-model="form.gender" placeholder="Select a Gender" :options="genders" class="mb-3" />
      <BaseListBox v-model="form.race" placeholder="Select a Race" :options="races" class="mb-3" />
      <BaseListBox v-model="form.faction" placeholder="Select a Faction" :options="factions" class="mb-3" />
      <BaseInput
        v-model="form.charisma"
        label="Charisma:"
        type="number"
        class="mb-3"
      />
      <BaseInput v-model="form.pace" label="Pace:" type="number" class="mb-3" />
      <BaseInput
        v-model="form.parry"
        label="Parry:"
        type="number"
        class="mb-3"
      />
      <BaseInput
        v-model="form.toughness"
        label="Toughness:"
        type="number"
        class="mb-3"
      />

      <div class="mb-3">
        <div class="input-group">
          <BaseInput
            v-model="attributes.name"
            label="Attribute Name:"
            type="text"
          />
          <BaseInput
            v-model="attributes.value"
            label="Attribute Value:"
            type="text"
          />
          <button
            type="button"
            class="btn btn-outline-light"
            @click.prevent="addAttribute"
          >
            Add
          </button>
        </div>
        <div v-if="attributes.items?.length">
          <ul class="list-group">
            <li
              class="list-group-item border-light"
              style="background: none !important"
              v-for="(item, index) in attributes.items"
              :key="index"
            >
              <div class="input-group">
                <BaseInput
                  v-model="item.name"
                  label="Attribute Name:"
                  :placeholder="`Attribute Name ${index + 1}`"
                  type="text"
                />
                <BaseInput
                  v-model="item.value"
                  label="Attribute Value:"
                  :placeholder="`Attribute Value ${index + 1}`"
                  type="text"
                />
                <button
                  type="button"
                  class="btn btn-outline-warning"
                  @click.prevent="updateAttribute(index)"
                >
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-outline-danger"
                  @click.prevent="deleteAttribute(index)"
                >
                  Delete
                </button>
              </div>
            </li>
          </ul>
        </div>
        <div v-else>
          <p>No attributes have been added yet.</p>
        </div>
      </div>

      <div class="mb-3">
        <div class="input-group">
          <BaseInput v-model="skills.name" label="Skill Name:" type="text" />
          <BaseInput v-model="skills.value" label="Skill Value:" type="text" />
          <button
            type="button"
            class="btn btn-outline-light"
            @click.prevent="addSkill"
          >
            Add
          </button>
        </div>
        <div v-if="skills.items?.length">
          <ul class="list-group">
            <li
              class="list-group-item border-light"
              style="background: none !important"
              v-for="(item, index) in skills.items"
              :key="index"
            >
              <div class="input-group">
                <BaseInput
                  v-model="item.name"
                  label="Skill Name:"
                  :placeholder="`Skill Name ${index + 1}`"
                  type="text"
                />
                <BaseInput
                  v-model="item.value"
                  label="Skill Value:"
                  :placeholder="`Skill Value ${index + 1}`"
                  type="text"
                />
                <button
                  type="button"
                  class="btn btn-outline-warning"
                  @click.prevent="updateSkill(index)"
                >
                  Update
                </button>
                <button
                  type="button"
                  class="btn btn-outline-danger"
                  @click.prevent="deleteSkill(index)"
                >
                  Delete
                </button>
              </div>
            </li>
          </ul>
        </div>
        <div v-else>
          <p>No skills have been added yet.</p>
        </div>
      </div>

      <BaseInput
        v-model="form.hindrances"
        label="Hindrances:"
        type="text"
        class="mb-3"
      />
      <BaseInput v-model="form.edges" label="Edges:" type="text" class="mb-3" />

      <div class="d-grid gap-2">
        <button type="submit" class="btn btn-outline-success">Create</button>
      </div>
      <p v-if="error">{{ error }}</p>
    </form>
  </div>
</template>
