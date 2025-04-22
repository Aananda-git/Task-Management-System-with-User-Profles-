<!-- components/Navbar.vue -->
<template>
  <nav class="navbar navbar-light bg-light px-3">
    <span class="navbar-brand mb-0 h1">Task Manager</span>
    <button class="btn btn-outline-danger" @click="logout">Logout</button>
  </nav>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const logout = () => {
  localStorage.removeItem('token')
  router.push('/')
}
</script>
