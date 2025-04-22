<template>
  <div>
    <Navbar />

    <div class="container mt-5">
      <h3 class="mb-4">Welcome to the Dashboard</h3>

      <!-- Action Buttons -->
      <div class="mb-4 d-flex flex-wrap gap-3">
        <router-link to="/create-profile" class="btn btn-outline-primary">
          Create New Profile
        </router-link>
        <router-link to="/create-task" class="btn btn-outline-success">
          Add New Task
        </router-link>
      </div>

      <!-- Profile Section -->
      <section class="mb-5">
        <ProfileList />
      </section>

      <!-- Task Section -->
      <section>
        <TaskList />
      </section>
    </div>
  </div>
</template>

<script lang="ts" setup>
import Navbar from '../components/Navbar.vue'
import ProfileList from '../components/ProfileList.vue'
import TaskList from '../components/TaskList.vue'
</script>
