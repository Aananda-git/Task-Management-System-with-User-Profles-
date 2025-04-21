<template>
  <div class="container mt-5">
    <h3>Welcome to the Dashboard</h3>
    <div class="mt-4 d-flex flex-column gap-2">
      <router-link to="/profiles" class="btn btn-outline-primary">Manage Profiles</router-link>
      <router-link to="/tasks" class="btn btn-outline-success">Manage Tasks</router-link>
      <router-link to="/create-profile" class="btn btn-outline-secondary">Create New Profile</router-link>
      <router-link to="/create-task" class="btn btn-outline-dark">Create New Task</router-link>
      <button class="btn btn-danger mt-3" @click="logout">Logout</button>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useRouter } from 'vue-router'

const router = useRouter()
const logout = () => {
  localStorage.removeItem('token')
  router.push('/')
}
</script>
