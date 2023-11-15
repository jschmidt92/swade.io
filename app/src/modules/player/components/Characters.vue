<script lang="ts" setup>
import avatar from '@/assets/default.jpg'
import { usePlayerData } from '../playerUtils.js'

const { characters } = usePlayerData()
</script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">
      <div class="d-flex flex-row justify-content-between align-items-center">
        Characters
        <router-link
          class="btn btn-sm btn-outline-success"
          to="/characters/create"
          >New</router-link
        >
      </div>
    </div>
    <div class="card-body">
      <ul
        class="list-item-group list-group-flush m-0 p-0"
        v-if="(characters ?? []).length > 0"
      >
        <li
          class="list-group-item"
          v-for="(character, index) in characters"
          :key="index"
        >
          <div class="d-flex flex-row justify-content-start align-items-center">
            <img
              :src="avatar"
              class="img-fluid me-3"
              alt="..."
              style="max-width: 15% !important"
            />
            <div>
              <p class="nav-link pb-0 mb-0">{{ character.name }}</p>
              <p class="text-capitalize text-muted pt-0 mt-0">
                {{ character.race }}
              </p>
            </div>
            <div class="ms-auto me-3">
              <router-link
                class="btn btn-sm btn-outline-info"
                :to="{
                  name: 'CharacterDetails',
                  params: { id: character.id }
                }"
                ><font-awesome-icon icon="fa-solid fa-eye"
              /></router-link>
              <router-link class="btn btn-sm btn-outline-warning mx-1" to=""
                ><font-awesome-icon icon="fa-solid fa-pen-to-square"
              /></router-link>
              <router-link class="btn btn-sm btn-outline-danger" to=""
                ><font-awesome-icon icon="fa-solid fa-trash"
              /></router-link>
            </div>
          </div>
        </li>
      </ul>
      <p class="card-text" v-else>You don't have any characters.</p>
    </div>
  </div>
</template>
