<script setup lang="ts">

defineProps<{ type: string; value: string; label: string }>()

const getDamageTypeClass = (type: string) => {
    const damageTypeClasses: Record<string, string> = {
        Inc: 'border-success',
        Wounds: 'border-danger',
        Fatigue: 'border-warning'
    }

    return `d-flex justify-content-center align-items-center border rounded-circle ${damageTypeClasses[type]}`
}
</script>

<template>
    <div class="d-flex flex-column text-center">
        <div :class="getDamageTypeClass(type)" style="width: 55px; height: 55px;">{{ value }}</div>
        <p class="card-text">{{ label }}</p>
    </div>
</template>
