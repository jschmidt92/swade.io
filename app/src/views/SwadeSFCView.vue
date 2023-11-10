<script lang="ts" setup>
import { ref } from 'vue'
import { VuePDF, usePDF } from '@tato30/vue-pdf'
import swade from '@/assets/swade-sfc.pdf'

const page = ref(1)
const { pdf, pages } = usePDF(swade)

const nextPage = () => {
  page.value = page.value < pages.value ? page.value + 1 : page.value
}

const prevPage = () => {
  page.value = page.value > 1 ? page.value - 1 : page.value
}
</script>

<template>
  <div class="col-md-6 offset-md-3">
      <div class="input-group mb-3">
          <button class="btn btn-light" @click="prevPage">PREV</button>
          <span class="d-flex justify-content-around align-items-center px-3"><input class="form-control" v-model="page" type="number" min="1" :max="pages" />/{{ pages }}</span>
          <button class="btn btn-light" @click="nextPage">NEXT</button>
      </div>
      <VuePDF :pdf="pdf" :page="page" fit-parent>
        <div class="text-dark ms-2">Loading...</div>
      </VuePDF>
  </div>
</template>
