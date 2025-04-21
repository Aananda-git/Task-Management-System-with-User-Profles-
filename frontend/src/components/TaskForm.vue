<template>
  <div class="container mt-4">
    <h4>Create or Update Task</h4>
    <form @submit.prevent="submitTask">
      <div class="form-group">
        <label for="title">Title</label>
        <input v-model="task.title" id="title" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <textarea v-model="task.description" id="description" class="form-control" required></textarea>
      </div>
      <div class="form-group">
        <label for="status">Status</label>
        <select v-model="task.status" id="status" class="form-control">
          <option value="PENDING">Pending</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="COMPLETED">Completed</option>
        </select>
      </div>
      <div class="form-group">
        <label for="due_date">Due Date</label>
        <input v-model="task.due_date" id="due_date" type="date" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="assigned_to">Assigned To</label>
        <select v-model="task.assigned_to" id="assigned_to" class="form-control" required>
          <option v-for="profile in profiles" :key="profile.id" :value="profile.username">
            {{ profile.username }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary mt-3">Save Task</button>
    </form>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import api from '../services/api'
import type { Task, Profile } from '../types'
import router from '../router'



const task = ref<Task>({
  title: '',
  description: '',
  status: 'PENDING',
  due_date: '',
  assigned_to: '', 
})

const profiles = ref<Profile[]>([])

const fetchProfiles = async () => {
  try {
    const res = await api.get('/profiles/')
    profiles.value = res.data.results || res.data
  } catch (err) {
    console.error('Failed to fetch profiles:', err)
  }
}

const submitTask = async () => {
  try {
    // If task.id exists, we are updating the task
    if (task.value.id) {
      await api.put(`/tasks/${task.value.id}/`, task.value)
    } else {
      // Otherwise, create a new task
      await api.post('/tasks/', task.value)
    }
    alert('Task saved successfully!')
    router.push('/tasks')
  } catch (err) {
    alert('Failed to save task.')
    console.error(err)
  }
}

fetchProfiles()
</script>
