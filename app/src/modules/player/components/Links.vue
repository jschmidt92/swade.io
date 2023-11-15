<script lang="ts" setup></script>

<template>
  <div class="card shadow-sm mb-3">
    <div class="card-header card-title bg-dark-subtle fs-5">Links</div>
    <div class="card-body">
      <ul class="nav flex-column">
        <li class="nav-item">
          <router-link class="link-info link-underline-opacity-0" to="/swade"
            >SWADE Manual</router-link
          >
        </li>
        <li class="nav-item">
          <router-link
            class="link-info link-underline-opacity-0"
            to="/swade-sfc"
            >SWADE SFC Manual</router-link
          >
        </li>
      </ul>
    </div>
  </div>
</template>
